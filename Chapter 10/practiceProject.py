# The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.

import random, logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails:\n')
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'heads'
else:
    toss = 'tails'
assert toss.lower() in ['heads', 'tails'], f'toss is {toss}. Should be heads or tails.'
logging.debug(f'toss is {toss}')
logging.debug(f'guess is {guess}')
if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again!\n')
    if toss == guess:
        logging.debug(f'toss is {toss}')
        logging.debug(f'guess is {guess}')
        print('You got it!')
    else:
        logging.debug(f'toss is {toss}')
        logging.debug(f'guess is {guess}')
        print('Nope. You are really bad at this game.')