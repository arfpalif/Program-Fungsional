import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = list(map(lambda x: x[1], data_transaksi))
jumlah_terjual = list(map(lambda x: x[2], data_transaksi))

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.scatter(harga_produk, jumlah_terjual, color='blue', label='Hubungan Harga dan Jumlah Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Scatter Plot Hubungan Harga dan Jumlah Produk Terjual')

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
fig, ax = plt.subplots()
produk_labels = list(map(lambda x: x[0], data_transaksi))
ax.bar(produk_labels, pendapatan_produk, color='green', alpha=0.7, label='Pendapatan Produk')
ax.set_ylabel('Pendapatan')
ax.set_title('Bar Chart Pendapatan Produk') 

plt.legend()
plt.show()
