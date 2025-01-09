import os

class Kendaraan():
    def __init__(self, nama = None, harga = None):
        self.nama = nama
        self.harga = harga
        self.__left = self.__right = None
        self.status=None

    def insert(self, nama, harga):
        if self.nama == None:
            self.nama = nama
            self.harga = harga
        elif self.nama > nama:
            if not self.__left:
                self.__left = Kendaraan(nama, harga)
            else:
                self.__left.insert(nama, harga)

        elif self.nama < nama:
            if not self.__right:
                self.__right = Kendaraan(nama, harga)
            else:
                self.__right.insert(nama, harga)
        else:
            print("Barang sudah ada")

    def inorder(self):
        items = []
        if self.__left:
            items +=self.__left.inorder()
        items.append(self)
        if self.__right:
            items +=self.__right.inorder()
        return items


    def SelectionSort(self):
        arr = self.inorder()
        n = len(arr)
        for i in range(0, n):
            p = i
            for j in range(i + 1, n):
                if arr[j].harga < arr[i].harga:
                    p = j
            temp = arr[p]
            arr[p] = arr[i]
            arr[i] = temp
        return arr

    def display(self):

        menus= self.SelectionSort()

        i = 1
        print("Daftar Kendaraan :\nno harga \t nama")
        for menu in menus:
            print(f"{i}. {menu.harga} \t {menu.nama}")
            i+=1
    def search(self,nama):

        try:
            if nama == self.nama:
                return self
            elif nama < self.nama:
                return self.__left.search(nama)
            elif nama > self.nama:
                return self.__right.search(nama)
            else:
                print("Kendaraan tidak ditemukan")
                return False
        except:
            print("Kendaraan tidak ditemukan")
            return False

    def dsearch(self, nama):
        r = self.search(nama)
        print(f"{r.harga} \t {r.nama}")
    def edit(self, newNama, harga):
        self.nama = newNama
        self.harga = harga
        print("Kendaraan berhasil diedit")

    def deleteNode(self, root, key):
        # Base case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.nama:
            root.left = self.deleteNode(root.__left, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.nama:
            root.__right = self.deleteNode(root.__right, key)
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.__left is None:
                return root.__right
            elif root.__right is None:
                return root.__left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.nama = self.minValue(root.__right)

            # Delete the inorder successor
            root.__right = self.deleteNode(root.__right, root.nama)

        return root

    def minValue(self, root):
        minv = root.nama
        while root.__left:
            minv = root.__left.nama
            root = root.__left
        return minv