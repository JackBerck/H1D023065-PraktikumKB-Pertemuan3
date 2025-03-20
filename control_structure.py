import random

# Membuat list data untuk menyimpan bilangan bulat secara acak menggunakan library random
data = [random.randint(1, 100) for _ in range(10)]

# Membuat pengondisian menggunakan struktur if-else untuk memeriksa panjang daftar
if len(data) > 5:
    print("Data memiliki lebih dari 5 elemen")
else:
    print("Data memiliki 5 elemen atau kurang")

# Melakukan perulangan for untuk mengiterasi daftar dan mencetak setiap elemen
for i in range(len(data)):
    print(f"Elemen data-{i+1}: {data[i]}")
