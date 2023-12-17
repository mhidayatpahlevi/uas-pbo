                
# LAPORAN UAS PBO
# BAB I 
# LATAR BELAKANG 
## 1.1 OOP
Pemrograman berorientasi objek atau Object Oriented Programming atau OOP adalah jenis pemrograman komputer di mana programmer mendefinisikan tipe data dari struktur data, dan juga jenis operasi (fungsi) yang dapat diterapkan pada struktur data. Kemudian, struktur data ini yang nantinya akan menjadi objek yang meliputi data dan fungsi.  Selain itu, programmer dapat menciptakan hubungan antar objek. Misalnya, karakteristik suatu objek dapat menurun dari objek lain. Definisi lain dari OOP adalah konsep pada pemrograman dengan mengidentifikasi kelas objek yang terkait erat dengan metode yang digunakan.  OOP menawarkan potensi untuk mengembangkan pemrograman ke tingkat abstraksi yang lebih tinggi. Oleh sebab itulah, OOP adalah model pemrograman terpopuler untuk membuat kode untuk sebagian besar karir pendidikan programmer.  Selain itu, konsep Object Oriented Programming digunakan untuk menyusun program perangkat lunak menjadi potongan-potongan kode blueprint yang sederhana dan dapat dipakai kembali untuk membuat instance objek individual. Ada banyak bahasa pemrograman yang bisa digunakan untuk membuat program yang berorientasi objek, misalnya JavaScript, C++, Java, dan Python.

Tak hanya berorientasi pada objek, model pemrograman ini juga bisa berorientasi pada kelas yang nantinya dipakai untuk membuat objek individual dalam programming. Apa itu class dalam dunia coding? Class merupakan blueprint atau bagian isi dari objek yang dibuat. Bagian ini memiliki fokus terhadap hal-hal umum, sehingga dapat memberikan model lebih spesifik. Misalnya kamu menggunakan kelas ‘Pohon’ ke dalam pemrograman kamu. Maka, karakteristik objek yang bisa saja terbentuk berdasarkan prinsip OOP adalah ‘Pohon Mangga’ dimana bentuk ini adalah turunan dari kelas induk ‘Pohon’. Dengan mendefinisikan set kelas yang mewakili dan merangkum objek dalam suatu program, class dapat diatur ke dalam modul. Tujuannya adalah untuk meningkatkan struktur dan organisasi program perangkat lunak. Dengan demikian, developer menggunakan OOP adalah sebagai alat ketika mereka membuat kode program yang kompleks. Hal ini dikarenakan dengan menggunakan OOP , susunan kode program lebih mudah dan ringkas. Konsep OOP dan Contohnya Secara garis besar Object Oriented Programming memiliki empat konsep dasar. Di antaranya enkapsulasi, abstraksi, pewarisan, dan polimorfisme. Sekalipun konsep-konsep ini tampak sangat kompleks, memahami kerangka kerja umum tentang cara kerjanya akan membantu kamu memahami dasar-dasar program komputer OOP. 

# BAB II 
# SOAL DAN PEMBAHASAN 
## 2.1 SOAL
1. Membuat Program untun generated password

## 2.2 Pembahasan
source code : 
    
    import random
    import string
    class PasswordGenerator:
    def __init__(self):
        self.choices = {
            '1': string.ascii_lowercase,
            '2': string.ascii_uppercase,
            '3': '()[]{};_#*-',
            '4': string.digits,
            '5': string.ascii_letters + string.digits + '()[]{};_#*-'
        }
        self.selected_types = []
        self.password_length = 0
        self.password = ''

    def get_user_input(self):
        print("Selamat datang di pembuat kata sandi acak!")
        print("Silakan pilih jenis karakter yang ingin Anda gunakan:")
        print("1. Huruf kecil")
        print("2. Huruf besar")
        print("3. Simbol")
        print("4. Angka")
        print("5. Gabungan dari semuanya")

        self.selected_types = input("Masukkan pilihan (pisahkan dengan spasi jika lebih dari satu): ").split()
        self.password_length = int(input("Masukkan panjang password yang diinginkan: "))

    def generate_password(self):
        if self.password_length < 6:
            print("Panjang password minimal harus 6 karakter.")
            return

        all_chars = ''
        for choice in self.selected_types:
            if choice in self.choices:
                all_chars += self.choices[choice]

        if not all_chars:
            print("Tidak ada pilihan karakter yang dipilih.")
            return

        self.password = "".join(random.sample(all_chars, self.password_length))
        print("Kata sandi yang dihasilkan:", self.password)
        # Penggunaan kelas PasswordGenerator
        password_creator = PasswordGenerator() 
        password_creator.get_user_input() 
        password_creator.generate_password()


luaran yang dihasilkan :

    Selamat datang di pembuat kata sandi acak!
    Silakan pilih jenis karakter yang ingin Anda gunakan:
    1. Huruf kecil
    2. Huruf besar
    3. Simbol
    4. Angka
    5. Gabungan dari semuanya
    Masukkan pilihan (pisahkan dengan spasi jika lebih dari satu): 1 3
    Masukkan panjang password yang diinginkan: 7
    Kata sandi yang dihasilkan: _cqeav}

penjelasan penggunaan kode :
1. Membuat Kelas PasswordGenerator:
    
        password_creator = PasswordGenerator()

   kode ini untuk membuat objek dari kelas PasswordGenerator. Ini menciptakan sebuah instansi dari kelas yang memungkinkan kita menggunakan semua metode dan atribut yang didefinisikan dalam kelas tersebut.
2. Mendapatkan Input Pengguna

         password_creator.get_user_input()
   
   Metode get_user_input() digunakan untuk meminta pengguna memilih jenis karakter yang ingin digunakan dalam kata sandi dan memasukkan panjang kata sandi yang diinginkan.
3. Menghasilkan Kata Sandi:

       password_creator.generate_password()
   Metode generate_password() akan menghasilkan kata sandi berdasarkan pilihan pengguna yang telah dimasukkan sebelumnya.

penjelasan input data :

1. Pilihan Jenis Karakter:
Pengguna diminta untuk memilih jenis karakter yang ingin mereka gunakan dalam kata sandi. Mereka diminta untuk memilih dari pilihan berikut:
Huruf kecil (1)
Huruf besar (2)
Simbol (3)
Angka (4)
Gabungan dari semuanya (5)
Pengguna diminta memasukkan pilihan mereka dengan memasukkan nomor-nomor ini (dipisahkan oleh spasi jika memilih lebih dari satu opsi).

2. Panjang Kata Sandi:
   Pengguna diminta memasukkan panjang kata sandi yang diinginkan.

penjelasan saat kode dijalankan :
1. Inisialisasi Kelas:
Objek password_creator dibuat, yang menginisialisasi atribut-atribut seperti choices, selected_types, password_length, dan password.
2. Meminta Input:
Pesan sambutan ditampilkan dan pengguna diminta memasukkan pilihan karakter dan panjang kata sandi melalui metode get_user_input().
3. Generasi Kata Sandi:
Metode generate_password() digunakan untuk menghasilkan kata sandi berdasarkan input yang diberikan pengguna.
Jika panjang kata sandi kurang dari 6 karakter, pesan kesalahan akan ditampilkan.
Jika tidak ada pilihan karakter yang dipilih, program memberikan pesan bahwa tidak ada karakter yang dipilih.
Jika input valid, kata sandi acak akan dihasilkan berdasarkan preferensi pengguna.
4. Menampilkan Kata Sandi:
Kata sandi acak yang dihasilkan akan ditampilkan di layar.

tampilan screenshot kode :
<div align="center">
  
![image](https://github.com/mhidayatpahlevi11/UAS-PBO/assets/150652795/06adb9b9-a11e-472c-8348-7196881620bf)
![image](https://github.com/mhidayatpahlevi11/UAS-PBO/assets/150652795/25ff971c-77bd-4c7f-88f0-4bff0e4f5637)
![image](https://github.com/mhidayatpahlevi11/UAS-PBO/assets/150652795/883b7303-7e5f-4c32-868c-438d02a9e772)

</div>

tampilan screenshot luaran :
<div align="center">
  
![image](https://github.com/mhidayatpahlevi11/UAS-PBO/assets/150652795/b0cf8afe-1644-4690-87f3-35e37c402197)

</div>

# BAB III
# KESIMPULAN DAN SARAN 
## 3.1 Kesimpulan 
Kesimpulan pada pembelajaran kali ini yaitu oop (object oriented programing) memudahkan kita untuk membuat program dimana di dalam oop terdapat class, object dan method 
# 3.2 Saran
untuk memahami kode python dalam oop perlu belajar lebih bnyak lagi dan lebih teliti lagi 

# Daftar Pustaka 

[1] [Syahrudin, A. N., & Kurniawan, T. (2018). Input dan output pada bahasa pemrograman python. Jurnal Dasar Pemograman Python STMIK, 20, 1-7.](https://www.researchgate.net/profile/Tedi-Kurniawan-2/publication/338385483_INPUT_DAN_OUTPUT_PADA_BAHASA_PEMROGRAMAN_PYTHON/links/5e10643392851c8364b029c3/INPUT-DAN-OUTPUT-PADA-BAHASA-PEMROGRAMAN-PYTHON.pdf)

[2] [Rahman, S., Sembiring, A., Siregar, D., Prahmana, I. G., Puspadini, R., & Zen, M. (2023). PYTHON: DASAR DAN PEMROGRAMAN BERORIENTASI OBJEK. Penerbit Tahta Media.](http://tahtamedia.co.id/index.php/issj/article/view/344)

[3] [Enterprise, J. (2019). Python untuk Programmer Pemula. Elex media komputindo.](https://books.google.com/books?hl=id&lr=&id=78SZDwAAQBAJ&oi=fnd&pg=PP1&dq=bahasa+python+&ots=gpQ8ci4nTU&sig=yLyeZbIiMVDitvryQxeFgfSktys)

anggota kelompok :
M Hidayat Pahlevi 
Annas zam zam
Faturrahman Athallah
