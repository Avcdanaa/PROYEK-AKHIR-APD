from utils import clear_screen
from data import produk

def lihat_stok():
    clear_screen()
    print("=== STOK PRODUK ===")
    if not produk:
        print("Belum ada produk.")
    else:
        print("-" * 50)
        for id_produk, data in produk.items():
            print(f"{id_produk}. {data['nama']:<20} | Stok: {data['stok']} | Rp{data['harga']:,}")
        print("-" * 50)

def tambah_stok():
    clear_screen()
    print("=== TAMBAH STOK ===")
    lihat_stok()
    try:
        id_produk = int(input("\nMasukkan ID produk: "))
        if id_produk not in produk:
            print("ID produk tidak ditemukan!")
            return
        tambahan = int(input("Jumlah stok yang ditambahkan: "))
        if tambahan < 0:
            print("Jumlah tidak boleh negatif!")
            return
        produk[id_produk]["stok"] += tambahan
        print(f"Stok untuk '{produk[id_produk]['nama']}' berhasil ditambah!")
    except ValueError:
        print("Input harus berupa angka!")