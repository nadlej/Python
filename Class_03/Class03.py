'''
    3.1:

    x = 2; y = 3; # Zapis działa ale powinno sie zadeklarowac w oddzielnych liniach, bez średniów
    if (x > y): # nawiast zbędny
        result = x; # zbędny średnik
    else:
        result = y; # zbędny średnik
    for i in "qwerty": if ord(i) < 100: print(i) #### Nie działa bo if potrzebuje nowej linii
    for i in "axby": print(ord(i) if ord(i) < 100 else i) # działa bo if w princie
'''

'''
    3.2:

    L = [3, 5, 4];  L = L.sort() #  L. sort() sortuje listę "w miejscu", wiec nie trzeba jej przypisywac
    # ponownie do zmiennej, ponadto l.sort() zwraca None gdy sortowanie sie uda, wiec tu otrzymamy w L == None
    x, y = 1, 2, 3 # nie można do dwóch zmiennych przypisać 3 wartości
    X = 1, 2, 3; X[1] = 4 # nie można nadpisać wartości
    X = [1, 2, 3]; X[3] = 4 # żądany index poza maksymalnym, osiągalnym indexem ( == 2)
    X = "abc"; X.append("d") # obiekty string nie mają atrybutu append, wystarczyło by dać X += "d"
    L = list(map(pow, range(8))) # brakuje drugiego argumentu do pow, czyli listy potęg
'''

'''
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
'''

def ThreeThree():
    print('3.')
    for i in range(0, 30):
        if i % 3 != 0:
            print(i)

'''
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią potęgę x.
Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby,
to program ma wypisać komunikat o błędzie i kontynuować pracę.
'''

def ThreeFour():
    while True:
        n = input('4. Number: ')

        if n == 'stop':
            break
        try:
            n = float(n)
            print(n, '', n**3)
        except:
            print('WRONG TYPE, TRY AGAIN')

'''
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo 
obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
Należy zbudować pełny string, a potem go wypisać.
'''

def ThreeFive():
    print('5. ')
    n = 12
    str1 = str2 = ''
    str1 += '|'

    for i in range(n):
        str1 += '....|'

    i = n * 5

    while i >= 0:
        if str1[i] == '|':
            str2 = str(int(i/5)) + str2
            if len(str(int(i/5))) > 1:
                i -= 2
            else:
                i -= 1
        else:
            str2 = " " + str2
            i -= 1

    str1 = str1 + '\n' + str2
    print(str1)

'''
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. 
'''

def ThreeSix():
    print('6. ')
    x = 4
    y = 2

    xline = "+"
    xline += "---+" * x
    yline = "|"
    yline = yline + (" " * 3 + "|") * x + "\n"
    line = ""

    for i in range(0,y):
       line += xline + "\n" + yline
    line += xline
    print(line)

'''
Dla dwóch sekwencji znaleźć: 
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
'''

def ThreeEight():
    print('8. ')
    L1 = [1, 2, 3, 4]
    L2 = [3, 4, 5, 6]

    print('L1: ', L1)
    print('L2: ', L2)

    L = list(set(L1).intersection(L2))
    print(L)
    L = list(set(L1).union(L2))
    print(L)

'''
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
'''

def ThreeNine():
    print('9. ')

    L = [[],[4],(1,2),[3,4],(5,6,7)]
    print('L: ',L)
    res = []
    for i in L:
        res.append(sum(i))

    assert res == [0,4,3,7,18]
    print(res)


'''
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) 
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
'''

def ThreeTen():
    print('10. ')
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

    s = 'MCMXCIX'
    print('Number: ', s)

    total = 0
    for i in range(len(s)):
        if i == len(s)-1:
            total += roman[s[i]]
        else:
            if i+1 < len(s):
                if roman[s[i]] >= roman[s[i + 1]]:
                    total += roman[s[i]]
                else:
                    total -= roman[s[i]]

    print(total)



def test():
    ThreeThree()
    ThreeFour()
    ThreeFive()
    ThreeSix()
    ThreeEight()
    ThreeNine()
    ThreeTen()

test()

