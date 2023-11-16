class AkunAdmin:
    def __init__(self):
        self.data_peserta = []

    def input_data_peserta(self, nama, nilai):
        peserta = {"ID": len(self.data_peserta), "Nama": nama, "Nilai": nilai}
        peserta["Hasil Akhir"] = "Lolos" if nilai >= 75 else "Tidak Lolos"
        self.data_peserta.append(peserta)

    def edit_nilai(self, id_peserta, nilai):
        if 0 <= id_peserta < len(self.data_peserta):
            self.data_peserta[id_peserta]["Nilai"] = nilai
            self.data_peserta[id_peserta]["Hasil Akhir"] = "Lolos" if nilai >= 75 else "Tidak Lolos"
            return True
        return False

    def tampilkan_data_peserta(self):
        print("Data Peserta:")
        for peserta in self.data_peserta:
            print(f"ID: {peserta['ID']}, Nama: {peserta['Nama']}, Nilai: {peserta['Nilai']}, Hasil: {peserta['Hasil Akhir']}")

class AkunPeserta:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_data_sendiri(self, data_peserta):
        print(f"Data Anda ({self.nama}):")
        for peserta in data_peserta:
            if peserta["Nama"] == self.nama:
                print(f"ID: {peserta['ID']}, Nilai: {peserta['Nilai']}, Hasil: {peserta['Hasil Akhir']}")

def main():
    admin = AkunAdmin()
    peserta1 = AkunPeserta("Peserta1")
    peserta2 = AkunPeserta("Peserta2")

    # Admin input data peserta
    admin.input_data_peserta("Peserta1", 80)
    admin.input_data_peserta("Peserta2", 60)

    # Admin tampilkan data peserta
    admin.tampilkan_data_peserta()

    # Admin edit nilai peserta
    admin.edit_nilai(0, 70)

    # Admin tampilkan data peserta setelah edit
    admin.tampilkan_data_peserta()

    # Peserta1 tampilkan data sendiri
    peserta1.tampilkan_data_sendiri(admin.data_peserta)

    # Peserta2 tampilkan data sendiri
    peserta2.tampilkan_data_sendiri(admin.data_peserta)

if __name__ == "__main__":
    main()
