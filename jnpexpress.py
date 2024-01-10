import datetime

now = datetime.datetime.now()

daftar_pengiriman = []

def kirim_paket():
    id_paket = int(input("Masukkan ID Paket: "))
    for paket in daftar_pengiriman:
        if paket['id_paket'] == id_paket:
            print("ID Paket sudah digunakan, masukkan ID Paket yang lain.")
            id_paket = int(input("Masukkan ID Paket: "))
    nama_pengirim = input("Masukkan Nama Pengirim: ")
    nama_penerima = input("Masukkan Nama Penerima: ")
    alamat = input("Masukkan Alamat Penerima: ")
    telepon_penerima = input("Masukkan Nomor Telepon Penerima: ")
    waktu_pesanan_dibuat = now.strftime("%d/%m/%Y %H:%M")

    paket = {
        "id_paket": id_paket,
        "nama_pengirim": nama_pengirim,
        "nama_penerima": nama_penerima,
        "alamat": alamat,
        "telepon_penerima": telepon_penerima,
        "status": "Belum Dikirim",
        "waktu_pesanan_dibuat": waktu_pesanan_dibuat
    }

    daftar_pengiriman.append(paket)
    print(f"Paket dengan ID {id_paket} telah ditambahkan. Nomor resi akan dikirim ke Nomor {telepon_penerima}")
    
def ubah_status_paket():
    id_paket = int(input("Masukkan ID Paket yang akan diubah statusnya: "))
    for paket in daftar_pengiriman:
        if paket['id_paket'] == id_paket:
            new_status = input("Masukkan status baru: ")
            paket['status'] = new_status
            print(f"Status paket dengan ID {id_paket} berhasil diubah menjadi: {new_status}.")
            return
    print(f"Paket dengan ID {id_paket} tidak ditemukan.")

def hapus_pengiriman():
    id_paket = int(input("Masukkan ID Paket yang akan dihapus: "))
    for paket in daftar_pengiriman:
        if paket['id_paket'] == id_paket:
            daftar_pengiriman.remove(paket)
            print(f"Paket dengan ID {id_paket} berhasil dihapus.")
            return
    print(f"Paket dengan ID {id_paket} tidak ditemukan.")

def histori_pengiriman():
    print("==================")
    print("Histori Pengiriman")
    print("==================")
    for paket in daftar_pengiriman:
        print(f"ID Paket: {paket['id_paket']}")
        print(f"Nama Pengirim: {paket['nama_pengirim']}")
        print(f"Nama Penerima: {paket['nama_penerima']}")
        print(f"Alamat Penerima: {paket['alamat']}")
        print(f"Nomor Telepon Penerima: {paket['telepon_penerima']}")
        print(f"Status: {paket['status']}")
        print(f"Waktu Pesanan Dibuat: {paket['waktu_pesanan_dibuat']}")
        print("---------------------------------------")

# Program Utama
while True:
    print("=============================")
    print("Selamat Datang di JNP Express")
    print("=============================")
    print("[1] Kirim Paket")
    print("[2] Ubah Status Paket")
    print("[3] Hapus Pesanan Pengiriman")
    print("[4] Histori Pengiriman")
    print("[5] Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        kirim_paket()
        lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Mohon masukkan pilihan dengan benar.")
            lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Pilihan tidak valid, program selesai.")
            break
    elif pilihan == '2':
        ubah_status_paket()
        lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Mohon masukkan pilihan dengan benar.")
            lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Pilihan tidak valid, program selesai.")
            break
    elif pilihan == '3':
        hapus_pengiriman()
        lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Mohon masukkan pilihan dengan benar.")
            lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Pilihan tidak valid, program selesai.")
            break
    elif pilihan == '4':
        histori_pengiriman()
        lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Mohon masukkan pilihan dengan benar.")
            lanjut = str(input("Ingin kembali ke menu awal? (y/n): "))
        if lanjut == 'y' :
            print("\n")
        elif lanjut == 'n':
            print("Terima Kasih telah menggunakan JNP Express.")
            print("\n")
            break
        else :
            print("Pilihan tidak valid, program selesai.")
            break
    elif pilihan == '5':
        print("Terima kasih telah menggunakan JNP Express.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")