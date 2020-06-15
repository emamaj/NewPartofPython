#obliczanie kapitału zgromadzonego na koncie w stosunku do stopy oprocentowania oraz ilości lat

print("Podaj stan początkowy konta:")
stankonta = float(input())

print("Podaj stopę oprocententowania:")
oproce = float(input())

print("Podaj ilość lat:")
lata = int(input())

kapital = stankonta * (1 + oproce * lata)

print("Po {} latach stan Twojego konta będzie wynosił: {} zł".format(lata, kapital))