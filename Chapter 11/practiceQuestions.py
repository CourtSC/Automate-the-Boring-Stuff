from random import randint


for i in range(10):
    spam = i
    assert spam < 10

eggs = 'hello'
bacon = 'goodbye'
assert eggs.lower() != bacon.lower()

# assert False

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

import logging
logging.basicConfig(filename = 'factorialCalcLog.md', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Info, Debug, Warning, Error, Critical

logging.disable(logging.CRITICAL)
