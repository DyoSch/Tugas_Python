import os
os.system('cls')

try:
    print("Selamat Datang di Aplikasi Perhitungan Nilai Mahasiswa\n")
    nilai_tugas = input("Silahkan Masukkan nilai Tugas Anda: ")
    nilai_uts = input("Silahkan Masukkan nilai UTS Anda: ")
    nilai_uas = input("Silahkan Masukkan nilai UAS Anda: ")
    nilai_akhir = 0.25 * float(nilai_tugas) + 0.35 * float(nilai_uts)  + 0.4 * float(nilai_uas)
    tipe_nilai = {
        (85, 100): "A",
        (80, 85): "A-",
        (75, 80): "B+",
        (70, 75): "B",
        (65, 70): "B-",
        (60, 65): "C+",
        (55, 60): "C",
        (50, 55): "C-",
        (30, 50): "D",
        (0, 30): "E"
    }
    for nilai, huruf in tipe_nilai.items():
        if nilai_akhir >= nilai[0] and nilai_akhir <= nilai[1]:
            print("\nNilai Akhir Anda:", nilai_akhir, "\nDalam Huruf:", huruf)
            break
        elif nilai_akhir < 0 or nilai_akhir > 100:
            print("\n//**Error: Nilai Akhir di luar rentang 0 - 100**//")
            break
except ValueError:
    print("\n//**Error: Nilai harus berupa Angka**//")