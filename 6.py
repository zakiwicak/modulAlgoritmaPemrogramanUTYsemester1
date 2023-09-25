import datetime
x = datetime.datetime.now()

# ini adalah inputan
# tetapi kerena waktu yang mepet saya buat langsung saja
nama = "naruto"
beli = "3 nasi goreng 1 es jeruk"
tagihan = "RP.40000"
Uang = "Rp.900000"
kembalian = "Rp.860000"


def struk():
    print('='*25)
    print("="*7, "STRUK", "="*7)
    print('='*25)
    print("="*3, nama)
    print("="*3, beli)
    print("="*3, tagihan)
    print("="*3, Uang)
    print("="*3, kembalian)
    print('='*25)
    print("pesanan dibuat pada =", x)
    print('='*25)


struk()
