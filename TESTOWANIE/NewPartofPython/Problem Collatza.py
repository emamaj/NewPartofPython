#Problem Collatza



def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    elif number % 2 == 1:
         number = number * 3 + 1
         print(number)
         return number

print('Podaj liczbę')
try:
    liczba = int(input())
    while True:
        liczba = collatz(liczba)
        if liczba == 1:
            break
except ValueError:
    print('Musisz podać liczbę całkowitą')
    print('')