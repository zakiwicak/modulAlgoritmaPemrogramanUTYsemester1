def hitung_nilai_akhir(ujian_harian1, ujian_harian2, uts, uas):
    bobot_ujian_harian = 0.15
    bobot_uts = 0.3
    bobot_uas = 0.4

    nilai_akhir = (ujian_harian1 * bobot_ujian_harian) + (ujian_harian2 *
                                                          bobot_ujian_harian) + (uts * bobot_uts) + (uas * bobot_uas)
    return nilai_akhir


def konversi_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 80:
        huruf = "A"
    elif nilai_akhir >= 60:
        huruf = "B"
    elif nilai_akhir >= 40:
        huruf = "C"
    elif nilai_akhir >= 20:
        huruf = "D"
    else:
        huruf = "E"

    return huruf


print("---Nilai Ke 1---")
ujian_harian1 = float(input("Nilai Harian : "))
print("---Nilai Ke 2---")
ujian_harian2 = float(input("Nilai Harian : "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

nilai_akhir = hitung_nilai_akhir(ujian_harian1, ujian_harian2, uts, uas)
huruf = konversi_nilai_huruf(nilai_akhir)

print("Total Nilai Yang Didapat : ", nilai_akhir)
print("Total Nilai Dalam Huruf :", huruf)
