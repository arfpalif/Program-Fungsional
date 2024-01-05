expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# 1. Fungsi untuk menambahkan pengeluaran baru ke dalam expenses
add_expense = lambda date, description, amount: expenses.append({'tanggal': date, 'deskripsi': description, 'jumlah': amount})

# 2. Fungsi untuk menghitung total pengeluaran harian menggunakan lambda expression
calculate_total_expenses = lambda date: sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == date)

# 3. Fungsi untuk menyaring pengeluaran berdasarkan tanggal tertentu menggunakan list comprehension
get_expenses_by_date = lambda date: [expense for expense in expenses if expense['tanggal'] == date]

# 4. Fungsi generator untuk menghasilkan laporan pengeluaran harian dalam bentuk string
generate_expenses_report = lambda: ("\n".join(f"{expense['tanggal']}: {expense['deskripsi']} - {expense['jumlah']}" for expense in expenses))

# 5. Semua fungsi di atas diubah menjadi lambda sesuai permintaan.

# 6. Main program (main function tidak akan menjadi pure function karena memodifikasi data global)
def main():
    # Menambahkan pengeluaran baru
    add_expense('2023-07-26', 'Makan Malam', 75000)
    
    # Menghitung total pengeluaran untuk tanggal tertentu
    total_expenses = calculate_total_expenses('2023-07-25')
    print(f"Total pengeluaran pada tanggal 2023-07-25: {total_expenses}")
    
    # Menyaring pengeluaran berdasarkan tanggal
    expenses_on_date = get_expenses_by_date('2023-07-26')
    print(f"Pengeluaran pada tanggal 2023-07-26:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - {expense['jumlah']}")

    # Menghasilkan laporan pengeluaran harian
    report = generate_expenses_report()
    print("\nLaporan Pengeluaran Harian:")
    print(report)

if __name__ == "__main__":
    main()