import random

nama = input('silakan masukan nama anda: ')

if nama:
    print(f'selamat datang {nama}')
    confrom = True
    while confrom :
        nomor1 = random.randint(10,20)
        nomor2 = random.randint(20,30)
        simbol = random.choice(['+','*','-'])
        soal = input(f'{nomor1} {simbol} {nomor2} = ')
        if simbol == '+':
            jawaban = nomor1 + nomor2
        elif simbol == '-':
            jawaban = nomor1 - nomor2
        elif simbol == '*':
            jawaban = nomor1 * nomor2
        if int(soal) == jawaban: 
            print('selamat anda benar')
            confrom = input("apakah anda ingin bermain lagi [y/n] :")
            if confrom == "y" :
                confrom = True
            else :
                confrom = False
                exit()
        else :
            print('anda salah')
            confrom = input("apakah anda ingin bermain lagi [y/n] :")
            if confrom == "y" :
                confrom = True
            else :
                confrom = False
                exit()
else:
    print('masukan nama anda dulu baru bermain')