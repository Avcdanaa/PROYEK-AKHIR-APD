import os
from datetime import datetime

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

def tampilkan_produk():
    """Menampilkan daftar produk dengan format rapi."""
    print("=== DAFTAR PRODUK ===")
    print("-" * 40)
    for id_produk, data in produk.items():
        print(f"{id_produk}. {data['nama']:<15} | Rp{data['harga']:,}")
    print("-" * 40)

def hitung_total(keranjang):
    """Menghitung total harga dari semua produk di keranjang."""
    return sum(item["harga"] for item in keranjang)

def tampilkan_keranjang(keranjang):
    """Menampilkan isi keranjang belanja."""
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    print("\n--- KERANJANG BELANJA ---")
    for i, item in enumerate(keranjang, 1):
        print(f"{i}. {item['nama']} - Rp{item['harga']:,}")

def struk_belanja(keranjang, uang_dibayar, diskon=0):
    """Menampilkan struk belanja."""
    clear_screen()
    print("=" * 30)
    print("         STRUK BELANJA")
    print("=" * 30)
    for item in keranjang:
        print(f"- {item['nama']:<20} Rp{item['harga']:,}")
    print("-" * 30)
    total = hitung_total(keranjang)
    if diskon > 0:
        print(f"Total Belanja          Rp{total:,}")
        print(f"Diskon ({diskon}%)         -Rp{int(total * diskon / 100):,}")
        total = total - int(total * diskon / 100)
    print(f"Total Bayar            Rp{total:,}")
    print(f"Uang Dibayar           Rp{uang_dibayar:,}")
    print(f"Kembalian              Rp{uang_dibayar - total:,}")
    print("=" * 30)
    print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Terima kasih telah berbelanja!")
    print("=" * 30)
    input("\nTekan Enter untuk kembali ke menu...")

def simpan_struk_ke_file(keranjang, uang_dibayar, diskon=0):
    """Opsional: Simpan struk ke file txt."""
    total = hitung_total(keranjang)
    if diskon > 0:
        diskon_rupiah = int(total * diskon / 100)
        total_akhir = total - diskon_rupiah
    else:
        diskon_rupiah = 0
        total_akhir = total

    nama_file = f"struk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("=" * 30 + "\n")
        f.write("         STRUK BELANJA\n")
        f.write("=" * 30 + "\n")
        for item in keranjang:
            f.write(f"- {item['nama']:<20} Rp{item['harga']:,}\n")
        f.write("-" * 30 + "\n")
        if diskon > 0:
            f.write(f"Total Belanja          Rp{total:,}\n")
            f.write(f"Diskon ({diskon}%)         -Rp{diskon_rupiah:,}\n")
        f.write(f"Total Bayar            Rp{total_akhir:,}\n")
        f.write(f"Uang Dibayar           Rp{uang_dibayar:,}\n")
        f.write(f"Kembalian              Rp{uang_dibayar - total_akhir:,}\n")
        f.write("=" * 30 + "\n")
        f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("Terima kasih telah berbelanja!\n")
    print(f"Struk disimpan di: {nama_file}")

def layanan_kasir():
    """Fitur pelayanan kasir: melayani pembeli satu per satu."""
    keranjang = []

    while True:
        clear_screen()
        print("=== LAYANAN KASIR ===")
        tampilkan_produk()
        tampilkan_keranjang(keranjang)
        print("\n0. Selesai & Checkout")
        print("99. Kembali ke Menu Utama")
        
        pilih = input("\nPilih produk: ").strip()

        if pilih == "0":
            if not keranjang:
                print("\nKeranjang masih kosong.")
                input("Tekan Enter untuk lanjut...")
                continue

            total = hitung_total(keranjang)
            print(f"\nTotal Belanja: Rp{total:,}")
            
            diskon = 0
            gunakan_diskon = input("Gunakan diskon? (y/n): ").lower()
            if gunakan_diskon == "y":
                try:
                    diskon = float(input("Masukkan persen diskon (misal: 10): "))
                    if diskon < 0 or diskon > 100:
                        print("Diskon tidak valid! Diskon diabaikan.")
                        diskon = 0
                except ValueError:
                    print("Input diskon tidak valid! Diskon diabaikan.")
                    diskon = 0

            while True:
                try:
                    uang = int(input("Masukkan uang pembayaran: Rp"))
                    total_akhir = total - int(total * diskon / 100)
                    if uang < total_akhir:
                        print("Uang tidak cukup! Silakan masukkan ulang.")
                    else:
                        break
                except ValueError:
                    print("Input harus berupa angka.")

            struk_belanja(keranjang, uang_dibayar=uang, diskon=diskon)

            simpan_struk = input("Simpan struk ke file? (y/n): ").lower()
            if simpan_struk == "y":
                simpan_struk_ke_file(keranjang, uang_dibayar=uang, diskon=diskon)

            keranjang.clear()
            break

        elif pilih == "99":
            print("Kembali ke menu utama...")
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