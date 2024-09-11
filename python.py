
#Úkol 1 DONE
name = "Sebastián"

#Úkol 2 DONE
surname = "Gargosch"

#Úkol 3 DONE
print (name+surname)

#Úkol 4 DONE
input("Zadejte svůj věk: ")

#Úkol 5 DONE

lenght_name = len(name)
lenght_surname = len(surname)

print("Délka jména:", lenght_name)
print("Délka příjmení:", lenght_surname)

#Úkol 9 DONE

answer = input("Vlož svůj věk: ")

while not answer.isdigit():
    print("Zadej jen celočíselnou hodnotu")
    answer = input("Vlož svůj věk: ")

print("Děkuji.")