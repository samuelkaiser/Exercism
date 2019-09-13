import math

def is_armstrong_number(number):
    digits = str(number)
    total = 0
    for digit in str(number):
        total += pow(int(digit), len(str(number)))

    if (total == number):
        return True
    else:
        return False
