
def TwoTen(x):
    words = x.split()
    print('Dlugosc: ', len(words))

def TwoEleven(x):
    word = list(x)
    word = '_'.join(word)
    print(word)

def TwoTwelve(x, n):
    print(x[0:n])
    print(x[-n:])

def TwoThirteen(x):
    words = x.split()
    word = ''.join(words)
    print(len(word))

def TwoFourteen(x):
    words = x.split()
    print(words)
    maxWord = max(words, key = len)
    print('MaxWord: ',maxWord)
    print('Length of MaxWord: ', len(maxWord))

def TwoFifteen(x):
    number = ''
    for i in range(0, len(x)):
        c = str(x[i])
        number += c
    print(number)

def TwoSixteen(x):
    word = x.replace('GvR','Guido van Rossum')
    print(word)

def TwoSeventeen(x):
    words = x.split()
    print('Sortowanie wedlug kolejnosci alfabetycznej: ')
    print(sorted(words))
    print('Sortowanie wedlug dlugosci: ')
    print(sorted(words, key = len))

def TwoEighteen(x):
    word = str(x)
    print(word.count('0'))

def TwoNineteen(x):
    words = [str(i) for i in x]
    word = ''

    for i in range(0,len(words)):
       if len(words[i]) == 1:
           word += words[i].zfill(3)
       elif len(words[i]) == 2:
           word += words[i].zfill(3)
       elif len(words[i]) == 3:
           word += words[i]

    print(word)


def test():

    print('2.10')
    word = 'Wydzial Fizyki \n Astronomii \t Informatyki \n\n Stosowanej'
    print(word)
    TwoTen(word)

    print('\n2.11')
    word = 'JezykPython'
    print(word)
    TwoEleven(word)

    print('\n2.12')
    word = 'Wydzial Fizyki Astronomii Informatyki Stosowanej'
    print(word)
    TwoTwelve(word,5)

    print('\n2.13')
    word = 'Wydzial Fizyki Astronomii Informatyki Stosowanej'
    print(word)
    TwoThirteen(word)

    print('\n2.14')
    word = 'Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line'
    print(word)
    TwoFourteen(word)

    print('\n2.15')
    word = [11, 22, 33, 44, 999, 2]
    print(word)
    TwoFifteen(word)

    print('\n2.16')
    word = 'Wydzial Fizyki Astronomii GvR InformatykiGvR Stosowanej'
    print(word)
    TwoSixteen(word)

    print('\n2.17')
    word = 'Wydzial Fizyki Astronomii Informatyki Stosowanej'
    print(word)
    TwoSeventeen(word)

    print('\n2.18')
    word = 19999999999990000111111100
    print(word)
    TwoEighteen(word)

    print('\n2.19')
    word = [11, 22, 7, 112, 7, 20]
    print(word)
    TwoNineteen(word)

test()