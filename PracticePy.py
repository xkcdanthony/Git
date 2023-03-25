# Anthony Cross
# 3/24/2023

""" Please read before using...

This program is not strong enough to provide a strong password, 
please use for educational purposes."""

import random

import string


length = int(input("\n How many characters would you like your password to be?: "))


lower = string.ascii_letters

upper = string.ascii_letters

num = string.digits

symbols = string.punctuation

all = lower + upper + num + symbols


temp = random.sample(all,length)

password = "".join(temp)

print(password)

input("Thank you for using this program your passcode has been generated! ")