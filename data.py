users = {
    "admin": {"password": "admin123", "role": "admin"},
    "udin": {"password": "1234", "role": "user"}
}

produk = {
    1: {"nama": "Kaos Lacoste", "harga": 250000, "stok": 25},
    2: {"nama": "Celana Rucas", "harga": 400000, "stok": 35},
    3: {"nama": "Jaket H&M", "harga": 550000, "stok": 24},
    4: {"nama": "Topi Nike", "harga": 150000, "stok": 20},
    5: {"nama": "Sepatu Adidas", "harga": 750000, "stok": 20}
}

penjualan = {id_prod: 0 for id_prod in produk}