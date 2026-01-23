# VARIABEL
# Variabel adalah penanda makna atau wadah penyimpanan data
# Struktur --> wadah = isi, bisa diisi teks atau angka
apples_in_a_basket = 100  # Integer (bilangan bulat)
my_cat_name = "Miu Miu Cahaya Asia"  # String (teks)
klepon = "jajanan pasar tradisional berupa bola-bola kecil kenyal berwarna hijau"
is_the_gossip_true = True  # Boolean (yes or no; yay or nay; True or False)
is_the_gossip_false = False  # Boolean (nulisnya harus True dan False aja)
pi = 3.14  # Float (bilangan desimal atau pecahan)

nama_depan = "Miu Miu"
nama_belakang = "Cahaya Asia"
nama_lengkap = nama_depan + " " + nama_belakang
hobi = miumiuing = "bermalas-malasan"
cita_cita = "juara catur se-Asia Pasifik"
makanan_favorit = "klepon"
minuman_favorit = "beras kencur 3 shots"
print("My name is " + nama_lengkap +
      " and I do love miumiuing which means " + hobi)
print("As a beautiful and a bougie cat, my favorite snack is " + makanan_favorit +
      ". Do you know " + makanan_favorit + ", darlin'? It's a " + klepon)

# DICTIONARY
# Dictionary, kumpulan data yang berpasangan antara kunci dan nilai (key: value)
# Dictionary ditulis dengan kurung kurawal {} dan setiap item dipisahkan koma
# Jadi gini. KEY (kunci/data unik): VALUE (nilai/arti, penjelasan, detail)
# Contoh KEY: Value --> "Stagflasi": "Keadaan inflasi yang sangat tinggi dan berkepanjangan"
# Praktik:
my_profil_gue = {
    "nama": nama_lengkap,
    "umur": "4 years young",
    "pekerjaan": "pewaris takhta utama Wangsa Cahaya Asia",
    "cita-cita": cita_cita,
    "hobi": miumiuing,
    "mafa": makanan_favorit,
    "mifa": minuman_favorit
}
print("BIODATA MY DIRI GUE")
print("Nama     :", my_profil_gue["nama"])
print("Umur     :", my_profil_gue["umur"])
print("Cita-cita    :", my_profil_gue["cita-cita"])

# KAIDAH PRINT I (berdasarkan cara)
# Ada dua cara melakukan print: a) Print Biasa (Zaman Lawas), b) Print F-String (Zaman Baru)
# a) Print Biasa Zaman Lawas --> print("nama saya " + nama_lengkap)
print("Nama Saya " + nama_lengkap +
      " dan saya adalah " + my_profil_gue["pekerjaan"])
# b) Print F-String Zaman Baru --> print(f"nama saya {nama_lengkap}")
# Cara pakai F-String: print(f"teks {variabel} teks {variabel}") --> setiap variabel pakai kurung kurawal
print(f"Saya {nama_lengkap} dan saya adalah {my_profil_gue['pekerjaan']}")
print(
    f"Whats'up my brok, akulah {nama_lengkap} sang {my_profil_gue['pekerjaan']}")
# Conclusion: Look at the different, it more simple and clean and slay with F-String. Makasih, F-String

# KAIDAH ENTER (\n)
# \n --> new line (baris baru)
print("Dear diary, \nWhy do I look fabulous today? \nJust like every other day.")
print(f"Anyway, Wangsa Cahaya Asia is the mastermind of {my_profil_gue['mafa']}\n"
      f"Imagine a world without {my_profil_gue['mafa']}, how sad would that be, darling?\n"
      f"Alas, people here are so... bizarre. And genius at the same time.\n"
      f"They mixed {my_profil_gue['mafa']} with sambel and called it as a Klepon Geprek Jeletot.\n"
      f"I can't even... \n"
      f"Imagine those chewy green balls with spicy sambel. \n"
      f"Ugh, humans are so weird sometimes.\n"
      f"Thank God, Tuhan Yang Maha Esa created me as a cat.\n")
