
"""
Stworzyć plik rekurencja.py i zapisać w nim funkcje z zadań 4.3 (factorial), 4.4 (fibonacci).
 Sprawdzić operacje importu i przeładowania modułu.
"""

def factorial(n):
    assert n >= 0

    fact = 1
    if n == 0 | n == 1:
        return fact
    else:
        for i in range(2, n + 1):
            fact *= i
    return fact



def fibonacci(n):
    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x1 = 0
        x2 = 1
        k = 0

        for i in range(2, n + 1):
            k = x1 + x2
            x1 = x2
            x2 = k

        return k
