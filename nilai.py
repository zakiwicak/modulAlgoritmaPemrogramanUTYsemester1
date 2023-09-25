def nilai_MK():
    print('---Nilai ke 1---')
    nilai1= int(input('Nilai Harian= '))

    print('---Nilai ke 2---')
    nilai2= int(input('Nilai Harian= '))

    rata_rata= (nilai1 + nilai2)*1/2
    print(rata_rata)

    nilai_UTS= int(input('Nilai UTS= '))
    nilai_UAS= int(input('Nilai UAS= '))
    print(rata_rata, nilai_UTS, nilai_UAS)

    total_nilai= (0.3 * rata_rata) + (0.3*nilai_UTS) + (0.4*nilai_UAS)
    print('---Total Nilai---')
    print('Total Nilai yang Didapat= ', total_nilai)

    if total_nilai == 0 and total_nilai < 20:
        print('Total Nilai dalam Huruf= E')
    elif total_nilai >= 20 and total_nilai < 40:
        print('Total Nilai dalam Huruf= D')
    elif total_nilai >= 40 and total_nilai < 60:
        print('Total Nilai dalam Huruf= C')
    elif total_nilai >= 60 and total_nilai < 80:
        print('Total Nilai dalam Huruf= B')
    elif total_nilai >= 80 and total_nilai <= 100:
        print('Total Nilai dalam Huruf= A')
    else:
        print('Nilai Tidak Valid')

nilai_MK()