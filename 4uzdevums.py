skaitlis = int(input(" Ievadi skaitli: "))

faktorials = 1
for i in range(1, skaitlis + 1):
    faktorials*=i

print(f"{skaitlis} faktorials ir {faktorials}")
