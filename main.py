from utils import clear_screen, tampilkan_header
from data import users

while True:
    clear_screen()
    tampilkan_header()
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        clear_screen()
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role.upper()}!")
            input("Tekan Enter untuk melanjutkan...")

            if role == "admin":
                from admin import menu_admin
                menu_admin(username)
            else:
                from user import menu_user
                menu_user(username)
        else:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")

    elif pilih == "2":
        clear_screen()
        print("=== REGISTER AKUN BARU ===")
        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        if username in users:
            print("Username sudah digunakan!")
        elif not username or not password:
            print("Username dan password tidak boleh kosong!")
        else:
            users[username] = {"password": password, "role": "user"}
            print("Akun berhasil dibuat! Silakan login.")
        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":
        clear_screen()
        print("Terima kasih telah mengunjungi Toko Baju Brand!")
        break

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")
