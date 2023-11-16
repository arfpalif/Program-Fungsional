import math
import os

def translasi(tx, ty):
    def inner_translasi(x, y):
        return x + tx, y + ty
    return inner_translasi

def dilatasi(sx, sy):
    def inner_dilatasi(x, y):
        return x * sx, y * sy
    return inner_dilatasi

def rotasi(sudut):
    def inner_rotasi(x, y):
        sudut_rad = math.radians(sudut)
        x_baru = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
        y_baru = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
        return x_baru, y_baru
    return inner_rotasi

# Titik awal
titik_awal = (3, 5)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

# Translasi
translasi_2_minus1 = translasi(2, -1)
titik_setelah_translasi = translasi_2_minus1(*titik_awal)
print(f"Koordinat setelah translasi: {titik_setelah_translasi}")

# Dilatasi
dilatasi_2_minus1 = dilatasi(2, -1)
titik_setelah_dilatasi = dilatasi_2_minus1(*titik_awal)
print(f"Koordinat setelah dilatasi: {titik_setelah_dilatasi}")

# Rotasi
rotasi_30_derajat = rotasi(30)
titik_setelah_rotasi = rotasi_30_derajat(*titik_awal)
print(f"Koordinat setelah rotasi: {titik_setelah_rotasi}")