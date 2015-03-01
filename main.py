__author__ = 'alberto'

from dittorier.tools.utils import measure_time
from dittorier.config import NUMBER_OF_GENERATIONS, CHROMOSOME_LENGTH, POPULATION_SIZE, logger, random, np


def single_signal_fitness():
    pass


def signal_population_fitness(current_population):
    pass


def signal_mutation(allele):
    rand_allele = random.randint(-1, 1)
    return rand_allele


@measure_time
def start_evaluation():
    logger.info("*" * 80)
    logger.info("*" * 80)
    logger.info("Starting Strassen Finder")
    logger.info("*" * 80)
    logger.info("Number of Generations: %s", NUMBER_OF_GENERATIONS)
    logger.info("Chromosome Length: %s", CHROMOSOME_LENGTH)
    logger.info("Population Size: %s", POPULATION_SIZE)
    logger.info("*" * 80)
    logger.info("*" * 80)


if __name__ == '__main__':
    result = start_evaluation()
