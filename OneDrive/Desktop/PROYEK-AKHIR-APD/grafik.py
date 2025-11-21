import matplotlib.pyplot as plt
from data import produk, penjualan

def tampilkan_grafik_penjualan():
    """Menampilkan grafik penjualan berdasarkan data penjualan."""
    if not penjualan or all(jumlah == 0 for jumlah in penjualan.values()):
        print("\nBelum ada data penjualan untuk ditampilkan.")
        input("Tekan Enter untuk kembali...")
        return

    nama_produk = []
    jumlah_terjual = []
    for id_prod in sorted(penjualan.keys()):
        nama_produk.append(produk[id_prod]["nama"])
        jumlah_terjual.append(penjualan[id_prod])

    plt.figure(figsize=(10, 6))
    plt.bar(nama_produk, jumlah_terjual, color='teal')
    plt.ylabel('Jumlah Terjual')  
    plt.title('Grafik Penjualan Produk')
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()
    plt.show()