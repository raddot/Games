import random

def guess_number(no):
    random_num = random.randint(1,no)
    guess = 0
    while guess != random_num :
        guess = int(input(f'Guess the number between 1 and {no} -> '))
        if guess < random_num:
            print('Too low! Guess number higher...')
        elif guess > random_num:
            print('Too high! Guess number lower...')

    print(f'Congratulations!!!... You guessed the number {random_num} correctly ')

guess_number(100)
