skaitlis = int(input("Ievadi skaitli: "))

summa = 0
for i in range(1, skaitlis + 1):
    summa += i

print(f"Summa no 1 līdz {skaitlis} ir {summa}.")