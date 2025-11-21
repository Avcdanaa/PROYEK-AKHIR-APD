# user.py
from utils import clear_screen, tampilkan_produk, hitung_total
from data import produk, keranjang_global

def menu_user(username):
    while True:
        clear_screen()
        print(f"=== MENU PENGGUNA: {username.upper()} ===")
        tampilkan_produk(produk)
        print("0. Checkout")

        pilih = input("\nPilih ID produk: ")

        if pilih == "0":
            checkout()
            break
        elif pilih.isdigit() and int(pilih) in produk:
            item = produk[int(pilih)]
            keranjang_global.append(item)
            print(f"{item['nama']} berhasil ditambahkan ke keranjang!")
        else:
            print("Input tidak valid!")
        input("\nTekan Enter untuk lanjut...")

def checkout():
    clear_screen()
    print("=== STRUK BELANJA ===")
    if not keranjang_global:
        print("Keranjang masih kosong.")
    else:
        tampilkan_produk({i+1: item for i, item in enumerate(keranjang_global)})
        total = hitung_total(keranjang_global)
        print(f"Total Belanja: Rp{total:,}")
    input("\nTekan Enter untuk keluar...")
