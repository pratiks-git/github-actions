# This programm checks if the provided integer is prime or not
# This file also has a unit test for checking he funtion

import math

def is_prime (a):
    flag = True
    for i in range(2, int(math.sqrt(a) + 1)):
        if (a % i == 0):
            flag = False
    return flag

def test_isprime():
    assert is_prime(5) == True
    assert is_prime(21) == False
    assert is_prime(23) == True