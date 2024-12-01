first = int(input("Vvedite chislo: "))
second = int(input("Vvedite chislo: "))
third = int(input("Vvedite chislo: "))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)