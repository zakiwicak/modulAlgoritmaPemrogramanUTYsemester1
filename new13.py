# Program Penghitung Diskon Belanja

# Fungsi untuk menghitung diskon
def hitung_diskon(total_belanja):
    diskon = 0
    if total_belanja > 150000:
        diskon = total_belanja * 0.1
    return diskon

# Meminta user untuk memasukkan total belanja
total_belanja = int(input("Masukkan total belanja: "))

# Menghitung diskon
diskon = hitung_diskon(total_belanja)

# Menampilkan total belanja dan diskon
print("Total Belanja: RP", total_belanja)
print("Diskon: RP", diskon)
print("Total Bayar: RP", total_belanja - diskon)
