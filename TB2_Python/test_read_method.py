from perpustakaan import Buku
from perpustakaan import read_buku

# Mengambil buku dengan id 1
buku = read_buku(1)

# Mencetak konten/halaman buku
print(Buku.read(buku, 1, 3))