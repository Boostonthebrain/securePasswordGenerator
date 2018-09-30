#secure password generator
#written by boostOnTheBrain
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-=+_?"

length = int(input('password length?'))
password = ''
for c in range(length):
  password += random.choice(characters)
print(password)

length = int(input('password length?'))
password = ''
for c in range(length):
  password += random.choice(characters)
print(password)

length = int(input('password length?'))
password = ''
for c in range(length):
  password += random.choice(characters)
print(password)

input("PRESS ENTER TO EXIT")