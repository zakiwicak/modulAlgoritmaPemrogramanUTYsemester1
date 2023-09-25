import sqlite3

# Membuat koneksi ke database UTY
db = sqlite3.connect("UTY.db")
cursor = db.cursor()

# Membuat tabel Mahasiswa
cursor.execute("""CREATE TABLE Mahasiswa (
                    NPM INTEGER,
                    nama TEXT,
                    prodi TEXT
                )""")

# Menambahkan record ke tabel Mahasiswa
cursor.execute("INSERT INTO Mahasiswa VALUES (1,'Naruto','IF')")
db.commit()

# Perintah untuk menambahkan data ke dalam tabel Mahasiswa
lagi = "y"
while lagi == "y":
    NPM_baru = input("Tambah no mhs: ")
    nama_baru = input("Tambah nama: ")
    prodi_baru = input("Tambah prodi: ")
    cursor.execute("INSERT INTO Mahasiswa (NPM, nama, prodi) VALUES (?, ?, ?)",
                   (NPM_baru, nama_baru, prodi_baru))
    db.commit()
    lagi = input("Input lagi (y/t): ")

# Menampilkan isi tabel Mahasiswa
cursor.execute("SELECT * FROM Mahasiswa")
print("Data Mahasiswa:")
for x in cursor.fetchall():
    print(x)

# Menutup koneksi ke database
db.close()
