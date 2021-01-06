import random
from math import sqrt


def all_random(n):
    return random.sample(range(n), n)


def partly_random(n):
    elements = [i for i in range(n)]
    for i in range(1, n):
        x = random.randint(0, 3)
        if x == 0:
            elements[i-1], elements[i] = elements[i], elements[i-1]
    return elements


def invert_partly_random(n):
    elements = partly_random(n)
    for i in range(int(n/2)):
        elements[i], elements[n-1-i] = elements[n-1-i], elements[i]
    return elements


def gaussian_random(n):
    return [random.gauss(0, 1) for _ in range(0, n)]


def repeated_random(n):
    k = int(sqrt(n))
    return [random.randint(0, k) for _ in range(0, n)]

