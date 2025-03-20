import random

# Membuat list data untuk menyimpan bilangan bulat secara acak menggunakan library random
data = [random.randint(1, 100) for _ in range(10)]

# Tampilkan value yang ada di dalam variabel list
print("Data:", data)

# Program untuk menyimpan frekuensi setiap bilangan dalam list data
frekuensi = {}
for nomor in data:
    if nomor in frekuensi:
        frekuensi[nomor] += 1
    else:
        frekuensi[nomor] = 1

# Tampilkan data frekuensi
print("Frekuensi:", frekuensi)