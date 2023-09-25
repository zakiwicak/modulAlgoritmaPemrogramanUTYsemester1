import datetime
now = datetime.datetime.now()
print("----")
print("waktu hari ini =", now)
print("Tahun =", now.year)
print("Bulan =", now.month)
print("Hari =", now.day)
print("jam =", now.hour)
print("menit =", now.minute)
print("detik =", now.second)

print("-------------")
print("1 minggu lalu adalah : ", datetime.timedelta(weeks=1))
print("100 hari yang lalu :", now-datetime.timedelta(days=100))
print("1 minggu kedepan : ", now+datetime.timedelta(weeks=1))
print("1000 hari dari sekarang: ", now + datetime.timedelta(days=1000))

print("-------------")
birthday = datetime.datetime(2020, 12, 14)

print("hitung mundur hari ulang tahun....", birthday)
print("-------------")
