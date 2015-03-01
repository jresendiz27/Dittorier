__author__ = 'alberto'

import sys
from PyQt4 import QtCore, QtGui

from dittorier.tools.utils import measure_time, chunks_with_index
from dittorier.config import NUMBER_OF_GENERATIONS, CHROMOSOME_LENGTH, POPULATION_SIZE, TEST_SIGNAL, FITNESS_WEIGHT, \
    EPSILON, logger, random, np
from dittorier.gui.Dittorier import Ui_Dialog
from dittorier.genetic.components import population, mutation, crosses, selectors
from multiprocessing import cpu_count, Pool, Array as mp_Array
from copy import copy
import time

result_array = mp_Array('i', len(TEST_SIGNAL))


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
        logger.debug("Find best for : %s", original_signal)
        min_value, max_value, average = min(original_signal), max(original_signal), np.mean(original_signal)

        signal_population = population.generate_population(min_value, max_value)
        signal_fitness = signal_population_fitness(signal_population, original_signal)
        # logger.debug("Population : %s", signal_population)
        # logger.debug("Fitness : %s", signal_fitness)
        for generation in range(0, NUMBER_OF_GENERATIONS):
            evaluation = np.abs(FITNESS_WEIGHT * CHROMOSOME_LENGTH - EPSILON)
            # logger.debug("Current evaluation : %s", evaluation)
            if signal_fitness[0] <= evaluation:
                # logger.debug("Copied to result array")
                copy_to_results_array(result_index, signal_population[0])
                break
            new_population = population.generate_new_population(signal_population, signal_fitness,
                                                                mutator=signal_mutation,
                                                                min_original=min_value, max_original=max_value,
                                                                average=average)
            # logger.debug("New population: %s", new_population)
            signal_population = sorted(new_population,
                                       key=lambda single: single_signal_fitness(single, original_signal),
                                       reverse=False)[0:POPULATION_SIZE]
            signal_fitness = signal_population_fitness(signal_population, original_signal)

        copy_to_results_array(result_index, signal_population[0])
        logger.debug("Original Signal: %s", original_signal)
        logger.debug("No better solution found at  %s generations : %s ", NUMBER_OF_GENERATIONS, signal_population[0])
    except Exception as e:
        logger.debug(e)
    return x


def result_callback(x):
    logger.info("Finishing all the work!")
    logger.info("X:     \n%s ", TEST_SIGNAL)
    logger.info("Result:\n%s", result_array[:])
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
    split_signal = chunks_with_index(TEST_SIGNAL, CHROMOSOME_LENGTH)
    pool = Pool()
    result = pool.map_async(find_best_for, split_signal, 1, result_callback)
    while True:
        if result.ready():
            #time.sleep(60)
            pool.close()
            pool.join()
            print result
            break


if __name__ == "__main__":
    start_cloning()
    # start_gui()
