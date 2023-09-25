import os
l = []
x =[]
y=[]
z=[]


def totBarang(banyak_pembelian, harga_satuan):
    total_per_barang= banyak_pembelian * harga_satuan
    return total_per_barang

def totDiskon(total_belanja):
    if total_belanja <= 150000:
        diskon=0
        harga_diskon = total_belanja * diskon
        return harga_diskon
    else:
        diskon=0.10
        harga_diskon = total_belanja * diskon
        return harga_diskon

def totBayar(total_per_barang, harga_diskon):
    bayar = total_per_barang - harga_diskon
    return bayar

def totKembalian(bayar, uang):
    kembalian = bayar - uang
    return kembalian

def menu():
    print("===========================================")
    print("==============Diskon Belanja===============")
    print("===========================================")

    nama_barang=str(input("Masukkan Nama Barang: "))
    banyak_pembelian= int(input("Masukkan Jumlah pembelian: "))
    harga_satuan=int(input("Masukkan Harga: "))
    total_barang= totBarang(banyak_pembelian, harga_satuan)
    
    
    

    l.append(nama_barang)
    x.append(banyak_pembelian)
    y.append(harga_satuan)
    z.append(total_barang)
   

    os.system('cls')
    tanya()

def tanya():
    print("Ingin Memesan Lagi? (y/t)")
    pertanyaan= str(input())
    if pertanyaan== 'Y' or pertanyaan== 'y':
        menu()
    elif pertanyaan=='T' or pertanyaan=='t':
        print('Nama Barang: ', l)
        print('Pembelian: ', x,' ',z)
        total_diskon= totDiskon(sum(z))
        tagihan= totBayar(sum(z),total_diskon)
        print('Tagihan: Rp.', tagihan)
        uang=int(input("Uang anda: Rp "))
        kembalian=uang-tagihan
        print('Kembalian: Rp.', kembalian)
    else:
        exit()
menu()