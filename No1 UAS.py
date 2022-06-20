nama = [["00001", "Benani Shalma", "Ilmu Sejarah"], ["00002", "I Putu Dika Dharma Brasika", "Teknologi Informasi"],["00003", "Putu Mahagita Kirana Prastuti", "Farmasi"]]

x = 0

print("Silahkan Pilih Nama Mahasiswa berikut :")
for i in nama:
    print(f"{x+1}. {nama[x][1]}")
    x = x + 1

user = int(input("Pilihan anda : "))

if user == 1:
    print(nama[0])
elif user == 2:
    print(nama[1])
elif user == 3:
    print(nama[2])
