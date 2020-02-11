wynik = 0
for i in range(10):
    #uzycie petli for nie obliguje do uzycia zmiennej x, program sie skraca. Zapis for i in range ozancza wykonaj petle 10 razy
    liczba = int(input("Podaj kolejna liczba:"))
    wynik += liczba
print (wynik)