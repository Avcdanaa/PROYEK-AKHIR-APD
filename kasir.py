from datetime import datetime  
from data import produk
from prettytable import PrettyTable
from colorama import Fore, init
from utils import clear_screen

init(autoreset=True)


def tampilkan_produk():
    """Menampilkan daftar produk dengan PrettyTable dan warna."""
    table = PrettyTable()
    table.field_names = [Fore.YELLOW + "ID", "Nama Produk", "Harga"]

    for id_produk, data in produk.items():
        table.add_row([
            Fore.CYAN + str(id_produk),
            Fore.GREEN + data['nama'],
            Fore.MAGENTA + f"Rp{data['harga']:,}"
        ])

    print(Fore.YELLOW + "\n=== DAFTAR PRODUK ===")
    print(table)


def hitung_total(keranjang):
    return sum(item["harga"] for item in keranjang)


def tampilkan_keranjang(keranjang):
    """Menampilkan isi keranjang belanja dengan tabel warna."""
    if not keranjang:
        print(Fore.RED + "Keranjang masih kosong.")
        return
    
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga"]

    for i, item in enumerate(keranjang, 1):
        table.add_row([
            Fore.CYAN + str(i),
            Fore.GREEN + item["nama"],
            Fore.MAGENTA + f"Rp{item['harga']:,}"
        ])

    print(Fore.YELLOW + "\n--- KERANJANG BELANJA ---")
    print(table)


def struk_belanja(keranjang, uang_dibayar):
    clear_screen()
    print(Fore.YELLOW + "=" * 35)
    print(Fore.YELLOW + "            STRUK BELANJA")
    print(Fore.YELLOW + "=" * 35)

    # ===== PrettyTable untuk isi belanja =====
    table = PrettyTable()
    table.field_names = ["Nama Barang", "Harga"]

    for item in keranjang:
        table.add_row([
            item["nama"],
            f"Rp{item['harga']:,}"
        ])

    print(table)

    total = hitung_total(keranjang)

    print("-" * 35)
    print(f"Total Bayar      : Rp{total:,}")
    print(f"Uang Dibayar     : Rp{uang_dibayar:,}")
    print(f"Kembalian        : Rp{uang_dibayar - total:,}")
    print("-" * 35)
    print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Terima kasih telah berbelanja!")
    print("=" * 35)

    input("\nTekan Enter untuk kembali ke menu...")


def simpan_struk_ke_file(keranjang, uang_dibayar):
    total = hitung_total(keranjang)

    nama_file = f"struk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("=" * 35 + "\n")
        f.write("            STRUK BELANJA\n")
        f.write("=" * 35 + "\n")

        for item in keranjang:
            f.write(f"{item['nama']:<20} Rp{item['harga']:,}\n")

        f.write("-" * 35 + "\n")
        f.write(f"Total Bayar      : Rp{total:,}\n")
        f.write(f"Uang Dibayar     : Rp{uang_dibayar:,}\n")
        f.write(f"Kembalian        : Rp{uang_dibayar - total:,}\n")
        f.write("-" * 35 + "\n")
        f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("Terima kasih telah berbelanja!\n")

    print(f"Struk disimpan di: {nama_file}")


def layanan_kasir():
    keranjang = []

    while True:
        clear_screen()
        print(Fore.YELLOW + "=== LAYANAN KASIR ===")
        tampilkan_produk()
        tampilkan_keranjang(keranjang)
        print("\na. Selesai & Checkout")
        print("b. Kembali ke Menu Utama")
        
        pilih = input("\nPilih produk: ").strip()

        if pilih == "a":
            if not keranjang:
                print(Fore.RED + "\nKeranjang masih kosong.")
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

            simpan_struk = input("Simpan struk ke file? (y/n): ").lower()
            if simpan_struk == "y":
                simpan_struk_ke_file(keranjang, uang_dibayar=uang)

            keranjang.clear()
            break

        elif pilih == "b":
            print("Kembali ke menu utama...")
            break

        elif pilih.isdigit() and int(pilih) in produk:
            item = produk[int(pilih)]
            keranjang.append(item)
            print(Fore.GREEN + f"{item['nama']} berhasil ditambahkan ke keranjang!")
            input("Tekan Enter untuk lanjut...")

        else:
            print(Fore.RED + "Input tidak valid!")
            input("Tekan Enter untuk lanjut...")


if __name__ == "__main__":
    layanan_kasir()
