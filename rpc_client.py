import xmlrpc.client

#menghubungkan ke server RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

#inputan dari pengguna
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

#manggil fungsi di server
hasil_tambah = proxy.tambah(a, b)
hasil_kali = proxy.kali(a, b)

#tampilkan hasil
print("Hasil penjumlahan:", hasil_tambah)
print("Hasil perkalian:", hasil_kali)
