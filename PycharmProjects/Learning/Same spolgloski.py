#wyliczanie samogłosek

print("Podaj slowo:")
slowo = input()


spol = 0
samo = 0

for x in slowo:
    if x in 'aeiouy':
        samo = samo + 1
    else:
        spol = spol + 1

print(samo)

