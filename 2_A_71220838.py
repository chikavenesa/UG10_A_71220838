print('=== Selamat datang di Toko Andi Tersenyum, selamat belanja! ===')
total = float(input('Total belanja : Rp. '))
diskondua = (total-(0.02*total))
diskonlima = (total-(0.05*total))
diskonsep = (total-(0.1*total))
if total>=1000000:
    print(f'Biaya yang harus dibayar setelah diskon adalah: Rp. {diskonsep}')
if total>=500000:
    print(f'Biaya yang harus dibayar setelah diskon adalah: Rp. {diskonlima}')
elif total<100000:
    print(f'Tidak ada diskon! Maka yang Anda bayarkan adalah: Rp. {total}')
elif total>=100000:
    print(f'Biaya yang harus dibayar setelah diskon adalah: Rp. {diskondua}')
