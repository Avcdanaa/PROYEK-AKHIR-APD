import os

produk = {
    1: {"nama": "Kaos Lacoste", "harga": 250000},
    2: {"nama": "Celana Rucas", "harga": 400000},
    3: {"nama": "Jaket H&M", "harga": 550000},
    4: {"nama": "Topi Nike", "harga": 150000},
    5: {"nama": "Sepatu Adidas", "harga": 750000}
}

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_produk_recursive(keys, index=0):
    """Menampilkan produk secara rekursif."""
    if index >= len(keys):
        return
    key = keys[index]
    data = produk[key]
    print(f"{key}. {data['nama']} - Rp{data['harga']:,}")
    tampilkan_produk_recursive(keys, index + 1)

def hitung_total(keranjang):
    """Menghitung total harga dari semua produk di keranjang."""
    total = 0  
    for item in keranjang:
        total += item["harga"]
    return total

def struk_belanja(keranjang, uang_dibayar=None):
    """Menampilkan struk belanja."""
    clear_screen()
    print("=== STRUK BELANJA ===")
    for item in keranjang:
        print(f"- {item['nama']} : Rp{item['harga']:,}")
    total = hitung_total(keranjang)
    print("------------------------------")
    print(f"Total belanja : Rp{total:,}")
    if uang_dibayar is not None:
        kembalian = uang_dibayar - total
        print(f"Uang Dibayar  : Rp{uang_dibayar:,}")
        print(f"Kembalian     : Rp{kembalian:,}")
    print("Terima kasih telah berbelanja!\n")
    input("Tekan Enter untuk kembali ke menu...")

def layanan_kasir():
    """Fitur pelayanan kasir: melayani pembeli satu per satu."""
    keranjang = []
    while True:
        clear_screen()
        print("=== LAYANAN KASIR ===")
        keys = list(produk.keys())
        tampilkan_produk_recursive(keys)
        print("0. Selesai & Checkout")
        print("99. Kembali ke Menu Utama")
        
        pilih = input("\nPilih produk: ")

        if pilih == "0":
            if not keranjang:
                print("Keranjang masih kosong.")
                input("Tekan Enter untuk lanjut...")
                continue

            total = hitung_total(keranjang)
            print(f"\nTotal Belanja: Rp{total:,}")
            
            while True:
                try:
                    uang = int(input("Masukkan uang pembayaran: Rp"))
                    if uang < total:
                        print("Uang tidak cukup! Silakan masukkan ulang.")
                    else:
                        break
                except ValueError:
                    print("Input harus berupa angka.")

            struk_belanja(keranjang, uang_dibayar=uang)
            break

        elif pilih == "99":
            break

        elif pilih.isdigit() and int(pilih) in produk:
            item = produk[int(pilih)]
            keranjang.append(item)
            print(f"{item['nama']} berhasil ditambahkan ke keranjang!")
            input("Tekan Enter untuk lanjut...")

        else:
            print("Input tidak valid!")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    layanan_kasir()