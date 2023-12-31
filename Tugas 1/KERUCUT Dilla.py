# Menghitung luas permukaan dan volume kerucut
# dibuat oleh fauzan ramadhan

# Jari-jari kerucut, tinggi kerucut, dan garis pelukis
jari_jari = 5
tinggi = 10
garis_pelukis = 12

# Mengimport nilai pi
from math import pi

# Menghitung luas permukaan kerucut
luas_permukaan = pi * jari_jari * (jari_jari + garis_pelukis)

# Menghitung volume kerucut
volume = (1/3) * pi * (jari_jari ** 2) * tinggi

# Menampilkan hasil
print("Luas Permukaan Kerucut: ", luas_permukaan)
print("Volume Kerucut: ", volume)
