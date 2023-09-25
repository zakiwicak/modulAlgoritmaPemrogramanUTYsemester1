import datetime

# Fungsi untuk menghitung total harga
def hitung_total(harga, jumlah):
    return harga * jumlah

# Meminta user untuk memasukkan data produk
nama_produk = input("Masukkan nama produk: ")
harga_produk = int(input("Masukkan harga produk: "))
jumlah_produk = int(input("Masukkan jumlah produk: "))

# Menghitung total harga
total_harga = hitung_total(harga_produk, jumlah_produk)

# Mendapatkan waktu sekarang
now = datetime.datetime.now()

# Menampilkan data transaksi
print("===================================")
print("Nama Produk:", nama_produk)
print("Harga Produk: RP", harga_produk)
print("Jumlah Produk:", jumlah_produk)
print("Total Harga: RP", total_harga)
print("Waktu Transaksi:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("===================================")
