import random

def computer_guess(no):
    low = 1;
    high = no;
    comp_guess = ' '
    while comp_guess != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        comp_guess = input(f'Is {guess} too High (H), too Low (L) or Correct (C)...').lower()
        if comp_guess == 'h':
            high = guess - 1;
        elif comp_guess == 'l':
            low = guess + 1;

    print(f'Congratulations!!! Computer guessed the number {guess} correctly')

computer_guess(100)
