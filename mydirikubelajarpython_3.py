# IF & ELSE & ELIF
# IF jika terjadi A, maka akan B
# Jika IF adalah False, maka lakukan ELSE
# ELIF = else if, jika ELSE (kondisinya) ada banyak
# Mekanismenya menggunakan boolean

# Logika IF, ELSE & ELIF
# IF membaca dari atas ke bawah
# Perintah (koding) harus jelas sejelas-jelasnya
# IF jadi pos pengecekan pertama
x = 10
if x > 5:
    print("Wow")
elif x > 8:
    print("Super Wow")
# Python mengeksekusi "Wow" karena 10 > 5
# Python mengabaikan ELIF karena nilai IF adalah True

# Praktik validitas
umur_validitas = 20
if umur_validitas >= 18:
    print("Dewasa")
else:
    print("Bocil")

# Praktik IF-ELSE cek suhu
# suhu 27-30 mantap, selain itu tidak mantap
# rentang1 --> x >= batas_min and x <= batas_max
# rentang2 --> batas_min <= x <= batas_max
suhu = 200
if suhu >= 27 and suhu <= 30:
    print("Hari yang mantap untuk beraktivitas di luar ruangan")
else:
    print("Hari yang tidak bersahabat")

# Praktik cek umur lanjutan
judul = "Kategori Usia"
print(judul.center(21, "-"))
print("balita = 1-5 \n"
      "anak-anak = 6-11 \n"
      "remaja = 12-25 \n"
      "dewasa = 26-45 \n"
      "lansia = >= 46")

nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))
if umur <= 0:
    print(f"{nama} berumur {umur} tahun? \n"
          f"{nama} bukan manusia!")
elif 1 <= umur <= 5:
    print(f"{nama} adalah balita")
elif 6 <= umur <= 11:
    print(f"{nama} adalah anak-anak")
elif 12 <= umur <= 25:
    print(f"{nama} adalah remaja")
elif 26 <= umur <= 45:
    print(f"{nama} adalah dewasa")
elif 46 <= umur <= 100:
    print(f"{nama} adalah lansia")
else:
    print(f"{nama} kemungkinan bukan manusia")

# CLAUDE, CHATGPT & GEMINI COMMENTARY
# Lebih ✨pythonic✨ kalau pakai rentang2 daripada rentang1
# Lebih baik sesuai urutan (kecil ke besar/sebaliknya)
# Lebih teliti:
# a) 1 < x < 5 ==> x = 2,3,4
# b) 1 <= x <= 5 ==> 1,2,3,4,5
# Else digunakan untuk selain IF dan ELIF
# Loophole: Akan terjadi eror jika pengguna:
# a) Memasukkan data string untuk umur terbilang, misal "dua tahun"
# b) Memasukkan data float (desimal), misal "10.1"
# Untuk klasifikasi lebih mantap belajar IF di dalam IF (Nested IF)
# Next stop: function, try-except, nested if
