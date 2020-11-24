lists = []
hitung = 1

while(True):
    nama = input("Nama : ")
    induk = input("NIM : ")
    latihan = input("Nilai tugas : ")
    exam1 = input("Nilai UTS : ")
    exam2 = input("Nilai UAS : ")
    akhir = (int(latihan)*30/100) + (int(exam1)*35/100) + (int(exam2)*35/100)

    tampung = []
    tampung.extend([hitung, nama, induk, latihan, exam1, exam2, akhir])
    lists.append(tampung)

    hitung += 1
    tanya = input("Tambah data (y/t) : ")
    if (tanya=='t'):
        break

print('=' * 81)
print("| NO |          Nama          |     Nim     |  Tugas  |  UTS  |  UAS  |  Akhir  |")
print('=' * 81)
for item in lists:
    print("|",'{:^2d}'.format(item[0]),"|"
          ,'{:^22}'.format(item[1]),"|"
          ,'{:^11}'.format(item[2]),"|"
          ,'{:^7}'.format(item[3]),"|"
          ,'{:^5}'.format(item[4]),"|"
          ,'{:^5}'.format(item[5]),"|"
          ,'{:^7.2f}'.format(float(item[6])),"|"
          )
print('=' * 81)
