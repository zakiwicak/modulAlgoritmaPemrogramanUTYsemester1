# Program Kalkulator Sederhana

# Fungsi untuk menambah dua bilangan
def tambah(x, y):
   return x + y

# Fungsi untuk mengurangi dua bilangan
def kurang(x, y):
   return x - y

# Fungsi untuk mengalikan dua bilangan
def kali(x, y):
   return x * y

# Fungsi untuk membagi dua bilangan
def bagi(x, y):
   return x / y


print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# Meminta user untuk memasukkan pilihan operasi
pilihan = input("Masukkan nomor pilihan (1/2/3/4): ")

num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))

if pilihan == '1':
   print(num1,"+",num2,"=", tambah(num1,num2))

elif pilihan == '2':
   print(num1,"-",num2,"=", kurang(num1,num2))

elif pilihan == '3':
   print(num1,"*",num2,"=", kali(num1,num2))

elif pilihan == '4':
   print(num1,"/",num2,"=", bagi(num1,num2))

else:
   print("Input yang Anda masukkan salah")