dbvirtual = [[], []]
n = int(input("masukkan nilai : "))

for i in range(1, n+1):
    if i % 2 == 0:
        dbvirtual[0].append(i)
        continue
    dbvirtual[1].append(i)

print("genap : ", len(dbvirtual[0]))
print("ganjil : ", len(dbvirtual[1]))
