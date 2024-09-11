
#Úkol 1
name = "sebastian"

#Úkol 2
surname = "gargosch"

#Úkol 3
print (name+surname)

#Úkol 4
input("Zadejte svůj věk: ")

#Úkol 9¨

answer = input("Vlož svůj věk: ")

while not answer.isdigit():
    print("Zadej jen celočíselnou hodnotu")
    answer = input("Vlož svůj věk: ")

print("Děkuji.")