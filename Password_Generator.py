import random

password_length = int(input("Enter the length of password - "))
string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(string,password_length))
print(password)