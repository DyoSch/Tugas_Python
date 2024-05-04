import os
os.system('cls')

# Diberikan sebuah bilangan integer n, dari masukan untuk semua nilai non negative integer
# di mana nilai i<n . Cetaklah nilai i^2

while(True):
    n = int(input("Masukkan nilai n: "))
    if n < 0 :
        print("Nilai n harus bilangan integer positif, ulangi\n")
    else:
        for i in range(n):
            print("i =", i,"->", i*i)
        break