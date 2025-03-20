import random
import json
import statistics

# Membuat list data untuk menyimpan bilangan bulat secara acak menggunakan library random
data = [random.randint(1, 100) for _ in range(10)]

# Menampilkan list data
print("Data:", data)

# Menggunakan library json untuk menyimpan list data ke dalam file dengan format json
with open('data.json', 'w') as f:
    json.dump(data, f)

# Menampilkan pesan jika data telah disimpan ke dalam file dengan nama data.json
print("Data telah disimpan ke dalam file data.json")

# Menggunakan library statistics untuk menghitung rata-rata dari data
mean = statistics.mean(data)
print("Rata-rata dari data adalah:", mean)
