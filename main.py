
#Úkol 1 DONE
name = "Sebastián"

#Úkol 2 DONE
surname = "Gargosch"

#Úkol 3 DONE
print (name+surname)

#Úkol 4 DONE
age = input("Zadej svůj věk: ")

while not age.isdigit():
    print("Zadej jen celočíselnou hodnotu")
    age = input("Vlož svůj věk: ")

#Úkol 5 DONE

lenght_name = len(name)
lenght_surname = len(surname)

print("Délka jména:", lenght_name)
print("Délka příjmení:", lenght_surname)

#Úkol 6 DONE
x = 6

#Úkol 7 DONE
for i in range(5):
    x += 3

#Úkol 8 DONE
print("Konečná hodnota po 5 cyklech:", x)

#Úkol 9 DONE
answerAge = input("Vlož svůj věk: ")

while not answerAge.isdigit():
    print("Zadej jen celočíselnou hodnotu")
    answerAge = input("Vlož svůj věk: ")
    print("Děkuji.")

#Úkol 10 DONE
import random

random_value = random.randint(1, 10)
print("Náhodná hodnota od 1 do 10 je:", random_value)

#BONUS DONE