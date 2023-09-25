import os
dbnama = []
dbtharga = []


def dtotalharga(harga, jumlah):
    return harga * jumlah


def totdis(totalbelanja):
    if totalbelanja <= 150000:
        diskon = 0
        hardis = totalbelanja * diskon
        return hardis
    else:
        diskon = 0.1
        hardis = totalbelanja * diskon
        return hardis


def tothar(total_harga, total_disk):
    return total_harga-total_disk


def tanya():
    lagi = str(input("masukkan lagi? (Y/T) : "))
    if lagi == "Y":
        os.system('cls')
        menu()
    elif lagi == "T":
        os.system('cls')
        struk()
    else:
        tanya()


def menu():
    print("========================================")
    print("====== aplikasi penghitung diskon ======")
    print("========================================")
    nama = str(input("masukkan nama barang     : "))
    harga = int(input("masukkan harga barang   :"))
    jumlah = int(input("masukkan jumlah barang :"))
    totalharga = dtotalharga(harga, jumlah)

    dbnama.append(nama)
    dbtharga.append(totalharga)

    os.system('cls')
    # windows
    tanya()


def struk():
    uanguser = int(input("masukkan uang :"))
    os.system('cls')
    print("=================================")
    print("========= Struk Belanja =========")
    print("=================================")
    print("nama barang  : ", dbnama)
    print("total harga  : ", sum(dbtharga))
    totaldis = totdis(sum(dbtharga))
    totharga = tothar(sum(dbtharga), totaldis)
    print("total diskon : ", totaldis)
    print("tagihan      : ", totharga)
    bayar = uanguser-totharga
    print("kembalian    : ", bayar)
    print("================================")


menu()
