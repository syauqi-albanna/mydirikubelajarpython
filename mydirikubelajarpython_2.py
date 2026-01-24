# STRING
# Cara mengolah string
# 1. Menghitung panjang string --> Len()
nama_depan = "Miu Miu"
nama_belakang = "Cahaya Asia"
nama_lengkap = name = f"{nama_depan} {nama_belakang}"
print(len(name))
# 2. Print karakter tertentu dalam string berdasarkan index (urutan)
print(name[0])  # string diawali dengan 0 --> 0 = M; 1 = i
print(name[-1])  # string minus untuk karakter terakhir --> -1 = a
print(name[0:4])  # slicing string --> index 0-3 (4 tidak termasuk)
print(name[8:])  # slicing string --> index 8 sampai akhir (8 termasuk)
# 3. Menambahkan karakter spesial dengan backslash (\)
print("They call me the \"Cahaya Asia\"")
# 4. F-string (lihat di mydirikubelajarpython_1.py atau di #STRING#1)
print(f"Akulah {nama_lengkap} sang pewaris takhta utama wangsa")
# 5. Mengubah gaya string
print(nama_lengkap.upper())  # mengubah jadi kapital
print(nama_lengkap.lower())  # mengubah jadi nonkapital
print(nama_lengkap.title())  # mengubah jadi kapital di awal kata
print(nama_lengkap.strip())  # menghapus spasi
print(nama_lengkap.find("Asia"))  # mencari posisi index karakter
print(nama_lengkap.replace("Asia", "Petromaks"))  # mengganti karakter
print(nama_lengkap.replace("i", "y"))  # mengganti karakter
# 6. Boolean di string, untuk mencari apakah ada karakter di string
print("Cah" in nama_lengkap)  # Jika ada, hasilnya True
print("Petromaks" in nama_lengkap)  # Jika tidak, hasilnya False
print("Cah" not in nama_lengkap)  # Karena ada, hasilnya False
print("Petromaks" not in nama_lengkap)  # Karena tidak ada, hasilnya True

# NUMERIK
# Olah angka anjirr
# 1. Operasi matematika dasar
print(1 + 1)  # penjumlahan
print(5 - 2)  # pengurangan
print(3 * 4)  # perkalian
print(40 / 6)  # pembagian
print(3 ** 3)  # pangkat
# 2. Operasi matematika agak mulai anu nih
print(40 // 6)  # pembagian dibulatkan ke bawah (floor division)
print(100 % 3)  # menampilkan sisa hasil bagi (modulus)
print(round(3.14159265, 2))  # pembulatan desimal
print(abs(-100))  # nilai mutlak/nilai absolut
# 3. Operasi matematika dengan math module
# WAJIB tulis <import math> sebelum pakai, preferensi di awal file
# Math module lainnya lihat di https://docs.python.org/3/library/math.html
# Math module dipakai untuk operasi matematika yang lebih kompleks, bukan yang ecek-ecek

# INPUT
# Input digunakan agar program bisa berinteraksi dengan pengguna
# Bikin koding gak boring, lebih interaktif gitu deh
nama_hamba = input("Siapakah namamu, wahai hamba Miu Miu sang Cahaya Asia? ")
print(f"Baiklah {nama_hamba}, mengabdilah di bawah Wangsa Cahaya Asia.")
# Sistem menunggu input dari pengguna, lalu menyimpannya di variabel nama_hamba dalam bentuk string mutlak
# Jika ingin mengubah tipe data input, bisa pakai fungsi bawaan seperti int atau float
# mengubah input string ke integer (bilangan bulat)
umur_hamba = int(input("Berapa umurmu, hambaku? "))
print(f"Hamba berumur {umur_hamba} tahun, wahai sang Miu Agung.")
