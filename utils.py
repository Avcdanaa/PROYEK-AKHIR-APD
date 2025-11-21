import os
from prettytable import PrettyTable

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header():
    print("=== SELAMAT DATANG DI TOKO BAJU BRAND ===")

def tampilkan_produk(produk):
    if not produk:
        print("Belum ada produk.")
        return
    table = PrettyTable(["ID", "Nama Produk", "Harga (Rp)"])
    for id_produk, data in produk.items():
        table.add_row([id_produk, data['nama'], f"{data['harga']:,}"])
    print(table)

def hitung_total(keranjang):
    return sum(item["harga"]for item in keranjang)