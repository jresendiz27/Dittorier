__author__ = 'alberto'

import sys
from PyQt4 import QtCore, QtGui

from dittorier.tools.utils import measure_time, chunks_with_index
from dittorier.config import NUMBER_OF_GENERATIONS, TEST_SIGNAL,CHROMOSOME_LENGTH, POPULATION_SIZE, FITNESS_WEIGHT, \
    EPSILON, logger, random, np
from dittorier.gui.Dittorier import Ui_Dialog
from dittorier.genetic.components import population
from dittorier.signal.audio.audio import read_audio_file, write_audio_file
from multiprocessing import cpu_count, Pool, Array as mp_Array
from copy import copy

result_array = mp_Array('i', 4000)
AUDIO_SIGNAL = []


def start_gui():
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())


def single_signal_fitness(single, original):
    accumulator = 0
    for index in range(0, len(single)):
        accumulator += np.abs(single[index] - original[index])
    return accumulator


def signal_population_fitness(current_population, original):
    fitness = []
    for single in current_population:
        fitness.append(single_signal_fitness(single, original))
    return fitness


def copy_to_results_array(start, content):
    copy_content = copy(content)
    for index in range(start + len(copy_content) - 1, start - 1, -1):
        result_array[index] = copy_content.pop()

    return True


def signal_mutation(allele, kwargs):
    flag = random.randint(0, 1)
    rand_values = []
    if flag:  # Mutation up
        rand_values.append(allele + int(kwargs['average']))
        rand_values.append(kwargs['max_original'])
    else:
        rand_values.append(kwargs['min_original'])
        rand_values.append(allele + int(kwargs['average']))
    rand_values = sorted(rand_values)
    return random.randint(rand_values[0], rand_values[1])


def find_best_for(x):
    try:
        result_index = x[0]
        original_signal = x[1:]
        min_value, max_value, average = min(original_signal), max(original_signal), np.mean(original_signal)
        signal_population = population.generate_population(min_value, max_value)
        signal_fitness = signal_population_fitness(signal_population, original_signal)
        for generation in range(0, NUMBER_OF_GENERATIONS):
            if signal_fitness[0] <= EPSILON:
                copy_to_results_array(result_index, signal_population[0])
                break
            new_population = population.generate_new_population(signal_population, signal_fitness,
                                                                mutator=signal_mutation,
                                                                min_original=min_value, max_original=max_value,
                                                                average=average)
            signal_population = sorted(new_population,
                                       key=lambda single: single_signal_fitness(single, original_signal),
                                       reverse=False)[0:POPULATION_SIZE]
            signal_fitness = signal_population_fitness(signal_population, original_signal)

        copy_to_results_array(result_index, signal_population[0])
    except Exception as e:
        logger.debug(e)
    return x


def result_callback(x):
    logger.info("Finishing all the work!")
    logger.info("X:     \n%s ", AUDIO_SIGNAL)
    logger.info("Result:\n%s", result_array[:])
    logger.info("Write Audio: %s ", write_audio_file('/home/alberto/Documents/PythonStuff/hola_hola_cloned.wav',result_array))
    return True


@measure_time
def start_cloning():
    logger.info("*" * 80)
    logger.info("*" * 80)
    logger.info("Starting Dittorier")
    logger.info("*" * 80)
    logger.info("Number of Generations per worker: %s", NUMBER_OF_GENERATIONS)
    logger.info("Chromosome Length: %s", CHROMOSOME_LENGTH)
    logger.info("Population Size per worker: %s", POPULATION_SIZE)
    logger.info("Number of workers: %s", cpu_count())
    logger.info("*" * 80)
    logger.info("*" * 80)
    AUDIO_SIGNAL = read_audio_file('/home/alberto/Documents/PythonStuff/holahola.wav')
    AUDIO_SIGNAL = AUDIO_SIGNAL[:len(AUDIO_SIGNAL) / 2]
    #AUDIO_SIGNAL = TEST_SIGNAL
    logger.info(len(AUDIO_SIGNAL))
    split_signal = chunks_with_index(AUDIO_SIGNAL, CHROMOSOME_LENGTH)
    pool = Pool()
    result = pool.map_async(find_best_for, split_signal, 1, result_callback)
    while True:
        if result.ready():
            pool.close()
            pool.join()
            print result
            break


if __name__ == "__main__":
    start_cloning()
