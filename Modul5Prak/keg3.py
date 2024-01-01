import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam centimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]

# TODO 1: Buat fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu

def kelompokkan_tinggi_badan(tinggi_badan, interval):
    kelompok = [i for i in tinggi_badan if interval[0] <= i < interval[1]]
    return kelompok


# TODO 2: Menghitung frekuensi tinggi badan dalam interval
interval = [(150, 160), (161, 170), (171, 180), (181, 190)]
frekuensi = [len(kelompokkan_tinggi_badan(tinggi_badan, i)) for i in interval]

# TODO 3: Visualisasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins=[150, 160, 170, 180, 190],
         color='blue', edgecolor='black', alpha=0.7, label='Data')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram Tinggi Badan')
plt.xticks([150, 160, 170, 180, 190])

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
mu, sigma = np.mean(tinggi_badan), np.std(tinggi_badan)
x = np.linspace(150, 190, 100)
pdf = norm.pdf(x, mu, sigma)
plt.plot(x, pdf * len(tinggi_badan) * np.diff(np.histogram(tinggi_badan,
         bins=[150, 160, 170, 180, 190])[1])[0], color='red', label='PDF (Normal Distribution)')
plt.legend()

plt.show()
