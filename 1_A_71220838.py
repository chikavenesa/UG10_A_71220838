nama = input('Masukkan nama mahasiswa: ')
nim = input('Masukkan NIM-nya: ')
if nim[0:2]=='71'and int(nim[2:4])<=22 and int(nim[2:4])>=20:
    print(f'{nama} merupakan mahasiswa informatika angakatan 20 hingga 22')
else: 
    print(f'{nama} bukan merupakan mahasiswa informatika angkatan 20 hingga 22')