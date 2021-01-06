from create_random_lists import *
import time


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


def insertsort(L, left, right):
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):  # od prawej do lewej (bez left)
            if L[j - 1] > L[j]:
                swap(L, j - 1, j)  # zamiana sąsiadów


def bubblesort(L, left, right):
    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j + 1]:
                swap(L, j + 1, j)


def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i + 1, right + 1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)


def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2  # wyznaczanie środka
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)  # scalanie


def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:  # mniejsze lub równe
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa część może mieć elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left + 1):
        L[left + i] = T[i]


def compare():
    n = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

    for N in n:
        oryginal_list = all_random(N)
        left, right = 0, len(oryginal_list)-1
        working_list = oryginal_list.copy()

        start = time.time()
        bubblesort(working_list, left, right)
        end = time.time()

        print("Czas sortowania metodą bubblesort dla", N, "elementów:", end-start)

        working_list.clear()
        working_list = oryginal_list.copy()

        start = time.time()
        insertsort(working_list, left, right)
        end = time.time()

        print("Czas sortowania metodą insertsort dla", N, "elementów:", end-start)

        working_list.clear()
        working_list = oryginal_list.copy()

        start = time.time()
        selectsort(working_list, left, right)
        end = time.time()

        print("Czas sortowania metodą selectsort dla", N, "elementów:", end-start)

        working_list.clear()
        working_list = oryginal_list.copy()

        start = time.time()
        mergesort(working_list, left, right)
        end = time.time()

        print("Czas sortowania metodą mergesort dla", N, "elementów:", end-start)
        print()


compare()

