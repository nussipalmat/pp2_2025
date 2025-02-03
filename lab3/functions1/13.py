import random

def guesser():
    print('Hello! What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.','Take a guess.\n')
    g = 1
    rand = random.randint(1, 20)

    while True:
        n = int(input())
        if n < rand:
            print('Your guess is too low.', 'Take a guess.\n')
            g += 1
        elif n > rand:
            print('Your guess is too high.', 'Take a guess.\n')
            g += 1
        else:
            print('Good job, {}! You guessed my number in {} guesses!'.format(name, g))
            break
guesser() 
