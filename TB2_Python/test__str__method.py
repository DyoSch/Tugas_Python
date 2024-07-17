from perpustakaan import Buku
from perpustakaan import read_buku

# Mengambil buku dengan id 1
buku = read_buku(1)

# Mencetak judul buku dan penulis
print(Buku.__str__(buku))