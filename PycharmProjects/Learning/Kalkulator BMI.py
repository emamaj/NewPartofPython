#Obliczanie BMI uzytkownika
print("Hej, obliczę Twoje BMI, podaj swoją wagę w kg:")
weight = float(input())
print("Teraz podaj proszę swój zwrost w cm")
heigh = float(input())
BMI = weight / (heigh ** 2)
print("Twoje BMI wynosi:", round(BMI, 6))