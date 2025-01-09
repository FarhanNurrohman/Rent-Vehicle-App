import datetime
class Peminjam():
    def __init__(self, nama, kendaraan, batasWaktu, noktp, totalharga):
        self.nama = nama
        self.noktp = noktp
        self.kendaraan = kendaraan
        self.batasWaktu = batasWaktu
        self.totalharga = totalharga


class Pinjam():
    def __init__(self):
        self.data = []
        self.front = self.rear = 0

    def banyakPeminjam(self):
        return self.rear

    def isEmpty(self):
        return (self.rear == 0)

    def display(self):
        i =1
        print("Daftar penyewa :\nno batas waktu \t kendaraan \t nama")
        for d in self.data:
            print(f"{i}. {d.batasWaktu} \t {d.kendaraan.nama} \t {d.nama}")
            i+=1

    def tambahPenyewa(self, nama, barang, waktu, noktp, totalharga):

        p = Peminjam(nama=nama, kendaraan=barang, batasWaktu=waktu, noktp=noktp, totalharga=totalharga)
        self.data.append(p)

        if self.rear==0:
            self.data = self.SelectionSort()




    def dequeue(self):
        if self.isEmpty():
            print("Print Queue is empty")
            return

        hapus = self.data.pop(0)
        self.rear -= 1
        return hapus

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return

    def search(self, nama):
        i = self.binarySearch(nama)
        if i == None:
            return None
        return self.data[i]

    def binarySearch(self, nama):
        try:
            low = self.front
            high = self.rear
            while low <= high:
                mid = low + (high - low) // 2
                if self.data[mid].nama == nama:
                    return mid
                elif self.data[mid].nama < nama:
                    low = mid + 1
                else:
                    high = mid - 1
                return None
        except:
            return None

    def delete(self, nama):
        i = self.binarySearch(nama)
        if i == None:
            return False
        return self.data.pop(i)
    def SelectionSort(self):
        arr = self.data
        n = len(self.data)
        for i in range(0, n):
            p = i
            for j in range(i + 1, n):
                if arr[j].nama < arr[i].nama:
                    p = j
            temp = arr[p]
            arr[p] = arr[i]
            arr[i] = temp
        return arr

