import os

# Curry function


def perkalian(a):
    def dengan(b):
        return a * b
    return dengan  # Mengembalikan fungsi inner operator

# Higher-Order Function (HOF)


def panggil_dengan_hof(fungsi, a, b):
    return fungsi(a)(b)

# Currying


def panggil_dengan_currying(fungsi_curry, a):
    def inner(b):
        return fungsi_curry(a)(b)
    return inner


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()


def main():
    while True:
        clear_terminal()
        # Pilihan pengguna
        pilihan = input("Pilih metode (1 untuk HOF, 2 untuk Currying): ")

        # Input dari pengguna
        a_input = float(input("Masukkan nilai a: "))
        b_input = float(input("Masukkan nilai b: "))

        # Contoh penggunaan berdasarkan pilihan
        if pilihan == "1":
            # Higher-Order Function (HOF)
            hasil_hof = panggil_dengan_hof(perkalian, a_input, b_input)
            print("Hasil HOF:", hasil_hof)
        elif pilihan == "2":
            # Currying
            fungsi_curry = panggil_dengan_currying(perkalian, a_input)
            hasil_currying = fungsi_curry(b_input)
            print("Hasil Currying:", hasil_currying)
        else:
            print("Pilihan tidak valid.")

        ulangi = input("Apakah Anda ingin mengulangi operasi? (y/n): ")
        if ulangi.lower() != 'y':
            break


if __name__ == "__main__":
    main()
