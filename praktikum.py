import os
os.system("cls")
print("PPROGRAM PYTHON PENJUMLAHAN LIST/ ARRAY ##")
print("============================================")
print()

n = int(input("Input Panjang  list : "))
print() 

print('input',n,'angka(dipisahh dengan enter): ');

x = []
for i in range(n):
    print('angka ke-', i+1 , ':' ,sep = '', end = '')
    x.append (int(input()))
    
print()

total = 0 
for i in range(n):
    total = total + x [i];
    
    
print('Total penjumlahan dari ',n,'angka tersebut adalah:',total)
print(25*"=")
print("MODIFIKASI DATA LIST")
print(25*"=")
print(f"panjang listnya adalah = {len(x)}")
print("angka pertama di list ini adalah : " , x[0])
if len(x)==2:
    print("datanya cuma ada 2")
elif len(x)==3:
    print("datanya cuma 3")
elif len(x)==1:
    print("datanya cuma 1")
else:
    print("datanya ini lebih dari 3 ")

