tambah_angka = lambda angka: angka 
 
print(tambah_angka(10)) 
 
klasifikasi_angka = lambda x: "Positif" if x > 0 else ("Negatif" if x < 0 else "Nol") 
def pencarian_angka(list_angka, find): 
    for num in list_angka: 
        if num == find: 
            return "found" 
    return "not found"