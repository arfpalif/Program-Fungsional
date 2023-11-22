import math

def create_transform_function(tx, ty, theta, sx, sy):
    def transform_point(point):
        # Translasi
        x_translated = point[0] + tx
        y_translated = point[1] + ty

        # Rotasi sejajar sumbu x positif sebesar theta derajat
        theta_rad = theta * (math.pi / 180)  # Konversi derajat ke radian
        x_rotated = x_translated * math.cos(theta_rad) - y_translated * math.sin(theta_rad)
        y_rotated = x_translated * math.sin(theta_rad) + y_translated * math.cos(theta_rad)

        # Perbesaran skala
        x_scaled = x_rotated * sx
        y_scaled = y_rotated * sy

        return [x_scaled, y_scaled]

    return transform_point

def calculate_line_equation(point1, point2):
    # Hitung persamaan garis dari dua titik
    m = (point2[1] - point1[1]) / (point2[0] - point1[0])  # Kemiringan (slope)
    c = point1[1] - m * point1[0]  # Perpotongan sumbu y (y-intercept)
    return m, c

# Titik awal A dan B
A_awal = [3, 4]
B_awal = [5, 6]

# Tampilkan persamaan garis sebelum transformasi
m_awal, c_awal = calculate_line_equation(A_awal, B_awal)
print(f'Persamaan garis sebelum transformasi: y = {m_awal:.2f}x + {c_awal:.2f}')

# Tentukan parameter transformasi
tx, ty = 2, -3
theta = 60
sx, sy = 1.5, 2

# Buat fungsi transformasi
transform_point = create_transform_function(tx, ty, theta, sx, sy)

# Transformasi titik A dan B
A_hasil = transform_point(A_awal)
B_hasil = transform_point(B_awal)

# Tampilkan persamaan garis setelah transformasi
m_hasil, c_hasil = calculate_line_equation(A_hasil, B_hasil)
print(f'Persamaan garis setelah transformasi: y = {m_hasil:.2f}x + {c_hasil:.2f}')
