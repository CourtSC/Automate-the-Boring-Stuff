#! python 3

import logging
logging.disable(logging.CRITICAL)

logging.basicConfig(filename = 'factorialCalcLog.md', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug(f'Start of fatorial({n})')
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug('End of factorial({n})')
    return total

print(factorial(5))
logging.debug('End of program')