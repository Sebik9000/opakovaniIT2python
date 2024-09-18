#OPRAVA 14:10 přesunul jsem ten import nahoru
import random

#Úkol 1
#Proměnná jméno
name = "Sebastián"

#Úkol 2 
#Proměnná příjmení
surname = "Gargosch"

#Úkol 3
#Vyhodí jméno a příjmení do konzole
print (name+surname)

#Úkol 4
#Zeptá se uživatele ať zadá věk a zkontroluje jestli je to číslo, jestli není tak mu to řekne ať zadá pouze číslo dokud ho nezadá a jestli to tak je tak ho to pustí dále
age = input("Zadej svůj věk: ")

while not age.isdigit():
    print("Zadej jen celočíselnou hodnotu")
    age = input("Vlož svůj věk: ")

#Úkol 5
#Vypíše délku jména a příjmení (kolik mají písmenek)
lenght_name = len(name)
lenght_surname = len(surname)

print("Délka jména:", lenght_name)
print("Délka příjmení:", lenght_surname)

#Úkol 6
#Promměnná x s hodnotou 6
x = 6

#Úkol 7
#Cyklus, který se opakuje 5x a pokaždé přičte k proměnné x hodnotu 3
for i in range(5):
    x += 3

#Úkol 8
#Vypíše konečnou hodnotu proměnné x po těch cyklech (6+3+3+3+3+3=21)
print("Konečná hodnota po 5 cyklech:", x)

#Úkol 9
#Zeptá se uživatele na věk a zkontroluje jestli je to číslo, jestli není tak mu to řekne ať zadá pouze číslo dokud ho nezadá a jestli to tak je tak mu to napíše "Děkuji."
answerAge = input("Vlož svůj věk: ")

while not answerAge.isdigit():
    print("Zadej jen celočíselnou hodnotu")
    answerAge = input("Vlož svůj věk: ")
    print("Děkuji.")

#Úkol 10
#Naimportuje knihovnu random a vygeneruje náhodnou hodnotu od 1 do 10 a tu pak napíše do konzole

random_value = random.randint(1, 10)
print("Náhodná hodnota od 1 do 10 je:", random_value)

#BONUS Hotov taky