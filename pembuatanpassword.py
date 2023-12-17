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
