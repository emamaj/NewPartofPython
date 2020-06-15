print("Podaj slowo")
slowo = input()

for x in slowo:
    if x in 'aeiouy':
        slowo = slowo.replace(x, "")

print(slowo)
