import MySQLdb

# Konfigurasi Database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'db': 'db_perpustakaan',
}

# Koneksi ke Database
conn = MySQLdb.connect(**db_config)