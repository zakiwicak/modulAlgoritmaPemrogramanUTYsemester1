import os


def tambah(a, b):
    return a+b


def kurang(a, b):
    return a-b

# sesuai halaman 78, menambah fungsi


def kali(a, b):
    return a*b


def bagi(a, b):
    return a/b


def pangkat(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def menu():
    print("=======Kalkulator PY=======")
    print("pilih jenis operasi dibawah")
    print("---------------------------")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Akar")
    print("6. Modulus")
    print("0. Keluar")
    print("===========================")

    pilihan = int(input('Masukan Menu: '))

    os.system('cls')

    if pilihan == 1:
        bil1 = int(input('Masukana Bilangan 1:'))
        bil2 = int(input('Masukana Bilangan 2:'))
        print("Jadi", bil1, "+", bil2, "=", tambah(bil1, bil2))
    elif pilihan == 2:
        bil1 = int(input('Masukana Bilangan 1:'))
        bil2 = int(input('Masukana Bilangan 2:'))
        print("Jadi", bil1, "-", bil2, "=", kurang(bil1, bil2))
    elif pilihan == 3:
        bil1 = int(input('Masukana Bilangan 1:'))
        bil2 = int(input('Masukana Bilangan 2:'))
        print("Jadi", bil1, "X", bil2, "=", kali(bil1, bil2))
    elif pilihan == 4:
        bil1 = int(input('Masukana Bilangan 1:'))
        bil2 = int(input('Masukana Bilangan 2:'))
        print("Jadi", bil1, ":", bil2, "=", bagi(bil1, bil2))
    elif pilihan == 5:
        bil1 = int(input('Masukana Bilangan 1:'))
        bil2 = int(input('Masukana Bilangan 2:'))
        print("Jadi", bil1, "^", bil2, "=", pangkat(bil1, bil2))
    elif pilihan == 6:
        bil1 = int(input('Masukana Bilangan 1:'))
        bil2 = int(input('Masukana Bilangan 2:'))
        print("Jadi", bil1, "%", bil2, "=", modulus(bil1, bil2))
    elif pilihan == 0:
        print("Program telah diakhiri")
        exit()
    else:
        print('Inputan tidak valid')


# perulangan
if __name__ == '__main__':
    while True:
        menu()
