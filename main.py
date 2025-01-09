from peminjaman import *
from kendaraan import *
import os
import datetime
os.system('cls')

penyewa = Pinjam()

motor = Kendaraan()
motor.insert('supra', 10000)
motor.insert('mio', 20000)
motor.insert('yamaha', 5000)
motor.insert('beat', 100000)

def inputAlphaValidation(text):
    return input(text).lower()

def inputNumValidation(text):
    while True:
        r = input(text)

        if r.isnumeric():
            return int(r)
        else:
            print("Masukkan anda tidak valid!")

def inputConfirmationValidation():
    while True:
        user = input("Apakah anda ingin lanjut?(Y/N):").lower()[0]

        if user == 'y':
            return True
        elif user == 'n':
            return False
        else:
            print("Inputan anda tidak valid!")

def tambahKendaraan():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    nama = inputAlphaValidation("Masukakan nama kendaraan:")
    harga = inputNumValidation("Masukkan harga(masukkan dalam bentuk angka):")
    motor.insert(nama=nama, harga=harga)

    print("Kendaraan berhasil ditambahkan!")

def editKendaraan():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    namaKendaraan = inputAlphaValidation("Massukkan nama Kendaraan yang dicari:")
    node = motor.search(namaKendaraan)
    if node:
        print("Edit kendaraan:")
        nama = inputAlphaValidation("Masukakan nama kendaraan yang baru:")
        harga = inputNumValidation("Masukkan harga yang baru(masukkan dalam bentuk angka):")
        node.edit(nama, harga)

def cariKendaraan():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    namaKendaraan = inputAlphaValidation("Massukkan nama kenaraan yang dicari:")

    while True:
        print("Daftar Kendaraan :\nharga \t nama")
        motor.dsearch(namaKendaraan)
        inp = inputConfirmationValidation()

        if inp:
            break

def hapusKendaraan():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    nama = inputAlphaValidation("Masukkan kenaraan yang anda ingin hapus:")
    r = motor.deleteNode(motor, nama)
    while True:
        if r == None:
            print("Kendaraan tidak terdaftar!")
        else:
            print("Kendaraan berhasil dihapus!")

        inp = inputConfirmationValidation()
        if inp:
            break



def daftarKendaraan():

    while True:
        print("="*63)
        print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
        print("="*63)
        motor.display()
        print("pilih aksi yang akan dilakukan: \n 1->Tambah  \n 2->Edit Kendaraan "
              "\n 3->Cari Kendaraan \n 4->Hapus kendaraan \n 5->Kembali")

        action = input(" Pilih action:")
        if action == '1':
            tambahKendaraan()
        elif action == '2':
            editKendaraan()
        elif action == '3':
            cariKendaraan()
        elif action == '4':
            hapusKendaraan()
        elif action == '5':
            break
            pesanan()
        else:
            print('Masukkan anda tidak valid!')

def cekstatus(kendaraanstatus):
    if kendaraanstatus != None:
        print('Kendaraan sudah ada yang menyewa')
        return True
    return False


def input_Peminjaman():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    nama = inputAlphaValidation("Masukkan nama penyewa: ")
    noktp = inputNumValidation("Masukkan No KTP: ")
    motor.display()
    kendaraan = motor.search(inputAlphaValidation("Masukkan kendaraan yang akan disewa: "))
    if kendaraan == False or cekstatus(kendaraan.status):
        inputConfirmationValidation()
        return
    waktu = inputNumValidation("Masukkan berapa lama menyewa(harian): ")
    t = datetime.datetime.now()
    kendaraan.status=True
    penyewa.tambahPenyewa(nama, kendaraan, f"{t.year}-{t.month}-{t.day+waktu}", noktp, kendaraan.harga*waktu)


def pengembalian():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    f = "%Y-%m-%d"
    nama = inputAlphaValidation("Nama penyewa: ")
    r = penyewa.delete(nama)
    denda = 0
    if r ==False:
        print("Nama penyewa tidak valid")
        inputConfirmationValidation()
    else:
        print('-' * 26)
        s = motor.search(r.kendaraan.nama)
        s.status=None
        t = datetime.datetime.now()
        k = datetime.datetime.strptime(r.batasWaktu, f)
        of = (k.day - t.day)
        if (t.day-k.day) > 0:
            denda = r.kendaraan.harga*of
        print(f"nama : \t\t {r.nama}")
        print(f"no KTP : \t\t {r.noktp}")
        print(f"nama kendaraan : \t\t {r.kendaraan.nama}")
        print(f"wktu pengembalian : \t {r.batasWaktu}")
        print(f"harga :\t\t {r.totalharga}")
        print(f"Total denda :\t\t {denda}")
        print('-'*26)
        print(f"harga :\t\t {r.totalharga +denda}")
        inputConfirmationValidation()



def cari_peminjam():
    print("="*63)
    print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
    print("="*63)
    nama = inputAlphaValidation("Nama penyewa: ")
    r = penyewa.search(nama)
    if r == None:
        print("penyewa tidak ditemukan!")

    else:
        print(f"nama : \t\t {r.nama}")
        print(f"no KTP : \t\t {r.noktp}")
        print(f"nama kendaraan : \t\t {r.kendaraan.nama}")
        print(f"waktu pengembalian : \t {r.batasWaktu}")
    inputConfirmationValidation()


def pesanan():
    while True :
        print("="*63)
        print("=== S E L A M A T  D A T A N G  D I  R E N T C A N G")
        print("="*63)
        penyewa.display()
        print("pilih aksi yang akan dilakukan: \n 1->Tambah Penyewa \n 2->Penyewa mengembalikan kendaraan \n 3->Cari Penyewa"
          "\n 4->Lihat Kendaraan \n 5->Exit")
        action = input(" Pilih action:")
        if action == '1':
            input_Peminjaman()
        elif action == '2':
            pengembalian()
        elif action == '3':
            cari_peminjam()
        elif action == '4':
            daftarKendaraan()
        elif action == '5':
            break
        else:
            print('maaf aksi tersebut tidak ada')

pesanan()






