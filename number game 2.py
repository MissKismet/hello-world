import numpy as np
number=np.random.randint(1,101)
print('Choose a number between 1 and 100')
guess=int(input('guess:'))
while guess != number:
    if guess < number:
        print('go higher')
    else:
        print('go lower')
    print('Try again')
    guess=int(input('guess:'))
print('You Win!')