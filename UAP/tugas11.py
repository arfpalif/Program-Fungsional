pangkat = lambda angka: (lambda x: x ** angka)
pangkat_dua = pangkat(2)
pangkat_3 = pangkat(3)

print (pangkat_dua(8))
print (pangkat_3(8))