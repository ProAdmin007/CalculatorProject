#Dit is een test porjectje voor een simpele calculator

print("----------------------")
print("THE BEST CALCULATOR!!!")
print("----------------------")

berekening = input("Wat voor berekening wil je doen? ")

plus = "+"
minn = "-"
keer = "*"
gedeeld = "/"

getal1 = int(input("Getal 1 graag: "))
getal2 = int(input("Getal 2 graag: "))

#reken gedeelte
optelling = getal1 + getal2
aftreking = getal1 - getal2
vermenigvuldiging = getal1 * getal2
deeling = getal1 / getal2

if berekening == plus:
    print("Uitkomst plus: ", optelling)
elif berekening == minn:
    print("Uitkomst min: ", aftreking)
elif berekening == keer:
    print("Uitkomst keer: ", vermenigvuldiging)
elif berekening == gedeeld:
    print("Uitkomst gedeeld: ", deeling)
else:
    print("Dat is niet een van de onderstuunde karakters: + - * /")

#print gedeelte
#    print("Optelling = ", optelling)
#    print("Min = ", min)
#    print("Keer = ", keer)
#    print("Deeling = ", deeling)
