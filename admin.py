# admin.py
from utils import clear_screen, tampilkan_produk
from data import produk

def tambah_produk():
    clear_screen()
    print("=== TAMBAH PRODUK ===")
    nama = input("Masukkan nama produk: ").strip()
    harga = input("Masukkan harga produk: ").strip()

    if not nama or not harga.isdigit():
        print("Input tidak valid!")
    else:
        id_baru = max(produk.keys()) + 1 if produk else 1
        produk[id_baru] = {"nama": nama, "harga": int(harga)}
        print(f"Produk '{nama}' berhasil ditambahkan!")

def ubah_produk():
    clear_screen()
    print("=== UBAH PRODUK ===")
    tampilkan_produk(produk)
    try:
        index = int(input("\nMasukkan ID produk yang ingin diubah: "))
        if index in produk:
            nama_baru = input("Nama baru (kosongkan jika tidak diubah): ").strip()
            harga_baru = input("Harga baru (kosongkan jika tidak diubah): ").strip()
            if nama_baru:
                produk[index]["nama"] = nama_baru
            if harga_baru.isdigit():
                produk[index]["harga"] = int(harga_baru)
            print("Produk berhasil diperbarui!")
        else:
            print("ID produk tidak ditemukan!")
    except:
        print("Input tidak valid!")

def hapus_produk():
    clear_screen()
    print("=== HAPUS PRODUK ===")
    tampilkan_produk(produk)
    try:
        index = int(input("\nMasukkan ID produk yang ingin dihapus: "))
        if index in produk:
            hapus = produk.pop(index)
            print(f"Produk '{hapus['nama']}' berhasil dihapus.")
        else:
            print("Produk tidak ditemukan!")
    except:
        print("Input tidak valid!")
