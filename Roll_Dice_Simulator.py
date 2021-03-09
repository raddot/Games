import random
while True:
    print('1. Roll the dice\n2.Exit')
    user = int(input("Select your choice - \n"))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    else:
        break