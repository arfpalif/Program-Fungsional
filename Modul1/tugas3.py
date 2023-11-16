# Sistem Penilaian Akhir Mahasiswa

def hitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, (nilai_uts, nilai_uas) in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai_uts, nilai_uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "Alif": (90, 60),
        "Bayu": (50, 20),
        "Tono": (10, 25),
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()