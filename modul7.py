nim = []
nama = []
asal = []


def pilihannya():
    print('\nSilahkan pilih menu yang tersedia : ')
    print ("1. masukan data.")
    print ("2. tampilkan data.")
    print ("3. hapus data.")
    print ("4. tambahkan data.")
    print ("5. update data.")
    print ("0. logout.")
    pilihan = int(input('Masukkan Pilihanmu : '))
    
    while (pilihan < 1 or pilihan > 4):
        print('Input yang dimasukkan salah, ulangi!')
        pilihan = int(input('\nMasukkan Pilihanmu : '))

    return pilihan
    
    pilihan = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
def masukkan_data():
    masnim = input("masukan nim : ")
    nim.append({'nim' : masnim})
    masnama = input("masukan nama : ")
    nama.append({'nama' : masnama})
    masasal = input("masukan asal : ")
    asal.append({'asal' : masasal})
        
        
        
def tampilkan_data() :
    penentu = True
    for i in range (len(nim)) :
        if penentu :
            print ("nim\tnama\tasal")
            print (nim[i]['nim'],'\t',nama[i]['nama'],'\t',asal[i]['asal'])
            penentu = False
            
def hapus_data():
        masnim = input("masukan nim : ")
        for i in range (len(nim)) :
            if masnim == nim[i]['nim'] :
                print (i)
                del nim[i]
                del nama[i]
                del asal[i]
                break
# def tambahkan_data():


# def update_data():



while pilihan == 1:
    pilihan = pilihannya()
    
    if(pilihan == 1):
        jalankan = masukkan_data()
    elif(pilihan == 2):
        jalankan = tampilkan_data()
    elif(pilihan == 3):
        jalankan = hapus_data()
    # elif(pilihan == 4):
    #     jalankan = 2

while pilihan == hapus_data:
    print("Terimakasih!!")
    break