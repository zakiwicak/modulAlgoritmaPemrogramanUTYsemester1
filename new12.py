# Program Penghitung Nilai Mata Kuliah

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_harian, nilai_uts, nilai_uas):
    nilai_akhir = (nilai_harian*0.3) + (nilai_uts*0.3) + (nilai_uas*0.4)
    return nilai_akhir

# Fungsi untuk menghitung nilai huruf dari nilai akhir
def hitung_nilai(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 75:
        return "B"
    elif nilai_akhir >= 65:
        return "C"
    elif nilai_akhir >= 55:
        return "D"
    else:
        return "E"

# Meminta user untuk memasukkan nilai harian, UTS, dan UAS
nilai_harian = float(input("Masukkan nilai harian (0-100): "))
nilai_uts = float(input("Masukkan nilai UTS (0-100): "))
nilai_uas = float(input("Masukkan nilai UAS (0-100): "))

# Menghitung nilai akhir
nilai_akhir = hitung_nilai_akhir(nilai_harian, nilai_uts, nilai_uas)

# Menampilkan nilai akhir dan nilai huruf
print("Nilai Akhir:", nilai_akhir)
print("Nilai Huruf:", hitung_nilai(nilai_akhir))
