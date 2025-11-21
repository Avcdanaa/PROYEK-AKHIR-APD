from utils import clear_screen, tampilkan_produk
from data import produk, penjualan
from stock import lihat_stok, tambah_stok
from grafik import tampilkan_grafik_penjualan

def tambah_produk():
    clear_screen()
    print("=== TAMBAH PRODUK ===")
    nama = input("Masukkan nama produk: ").strip()
    harga = input("Masukkan harga produk: ").strip()
    stok = input("Masukkan stok awal: ").strip()

    if not nama or not harga.isdigit() or not stok.isdigit():
        print("Input tidak valid!")
    else:
        id_baru = max(produk.keys()) + 1 if produk else 1
        produk[id_baru] = {"nama": nama, "harga": int(harga), "stok": int(stok)}
        penjualan[id_baru] = 0
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
            stok_baru = input("Stok baru (kosongkan jika tidak diubah): ").strip()
            if nama_baru:
                produk[index]["nama"] = nama_baru
            if harga_baru.isdigit():
                produk[index]["harga"] = int(harga_baru)
            if stok_baru.isdigit():
                produk[index]["stok"] = int(stok_baru)
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
            penjualan.pop(index, None)
            print(f"Produk '{hapus['nama']}' berhasil dihapus.")
        else:
            print("Produk tidak ditemukan!")
    except:
        print("Input tidak valid!")

def menu_admin(username):
    while True:
        clear_screen()
        print("=== MENU ADMIN ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Lihat Stok")
        print("6. Tambah Stok")
        print("7. Grafik Penjualan") 
        print("8. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear_screen()
            tampilkan_produk(produk)
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            tambah_produk()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "3":
            ubah_produk()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "4":
            hapus_produk()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "5":
            lihat_stok()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "6":
            tambah_stok()
            input("\nTekan Enter untuk kembali...")
        elif pilih == "7":
            tampilkan_grafik_penjualan()
        elif pilih == "8":
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")
