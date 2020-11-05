"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
"""


def FourTwoA(x):
    assert x > 0

    n = x
    str1 = str2 = ''
    str1 += '|'

    for i in range(n):
        str1 += '....|'

    i = n * 5

    while i >= 0:
        if str1[i] == '|':
            str2 = str(int(i / 5)) + str2
            if len(str(int(i / 5))) > 1:
                i -= 2
            else:
                i -= 1
        else:
            str2 = " " + str2
            i -= 1

    str1 = str1 + '\n' + str2
    return str1


def FourTwoB(x, y):
    assert x, y > 0

    xline = "+"
    xline += "---+" * x
    yline = "|"
    yline = yline + (" " * 3 + "|") * x + "\n"
    line = ""

    for i in range(0, y):
        line += xline + "\n" + yline
    line += xline
    return line


"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
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


"""
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
"""


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


"""
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
 Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
"""


def odwracanieA(L, left, right):
    assert left <= right

    i = (right - left) / 2

    while i > 0:
        L[left], L[right] = L[right], L[left]

        left += 1
        right -= 1
        i -= 1

    return L


def odwracanieB(L, left, right):
    if left > right:
        return L
    else:
        L[left], L[right] = L[right], L[left]

    return odwracanieB(L, left + 1, right - 1)


"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
 Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""


def sum_seq(sequence):
    count = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            count += sum_seq(x)
        else:
            count += x

    return count


"""
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""


def flatten(sequence):
    L = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            L.extend(flatten(x))
        else:
            L.append(x)

    return L


def test():
    print('4.2')
    print(FourTwoA(12))
    print(FourTwoB(4, 4))
    print('4.3')
    print(factorial(6))
    print('4.4')
    print(fibonacci(12))
    print('4.5')
    L = [0, 1, 2, 3, 4, 5]
    print(L)
    print(odwracanieA(L, 1, 4))
    L = [0, 1, 2, 3, 4, 5]
    print(odwracanieB(L, 1, 4))
    print('4.6')
    L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print(L)
    print(sum_seq(L))
    print('4.7')
    print(L)
    print(flatten(L))


test()
