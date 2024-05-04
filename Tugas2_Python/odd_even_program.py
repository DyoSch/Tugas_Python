import os
os.system('cls')

# Buatlah program untuk mendeteksi Ganjil genap, lalu program akan mengambil nilai 
# ganjil saja dan mencetak nilai kuadratnya

while(True):
    angka = int(input("Masukkan angka: "))
    if angka < 0 :
        print("Nilai n harus bilangan integer positif, ulangi\n")
    else:
        for i in range(angka):
            if (i%2 == 1 or i == 0):
                print("i =", i,"->", i*i)
            else:
                continue
        break