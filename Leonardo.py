# Nama : Leonardo Star Berutu
# Nim : 190402155
# Ujian Akhir Semester Pemrograman Komputer TE-D

# section 1 : Membuat dengan hasil print ('str', 'float', 'int')
L = "Labu"
P = 3.0
D = 5
print(L,P,D) # Hasil (Labu 3.0 2)
print(L) # Hasil(Labu)
print(P) # Hasil(3.0)
print(D) # Hasil (5)

# section 2 : Menentukan tipe dari hasil print
K = 8.4, 2.9
O = 7 , 57
M = "Kelas", "Teknik"
P = 7.0
U = 3
T = "Elektro"
E = 4.0
R = 6.9
print(type(K)) # <class 'tuple'>
print(type(O)) # <class 'tuple'>
print(type(M)) # <class 'float'>
print(type(P)) # <class 'float'>
print(type(U)) # <class 'str'>
print(type(T)) # <class 'str'>
print(type(E)) # <class 'int'>
print(type(R)) # <class 'int'> 

# section 3 : Python Number
# koordinat di titik A (4, 8)
x,y = 4, 8
y,x = 8, 4
print(x,y) # 4 8
print(y,x) # 8 4

# section 4 : Memotong huruf pada kalimat berdasarkan peletakkan huruf
Leo = "Saya mahasiswa teknik elektro usu"
print(Leo) # Saya mahasiswa teknik elektro usu
print(Leo[::-3]) # u tlkk samy
print(Leo[3]) # a
print(Leo[3:]) #a mahasiswa teknik elektro usu 
print(Leo.upper())
print(Leo.lower())
print(Leo.replace("S","m"))

# section 5 : Pyhton List
list1 = [1,3,5,7,9,11,13]
print(list1)
data1 = list1[0]
print(data1)
data2 = list1[-2]
print(data2) 

# section 6 : Kombinasi python list
Mobil = ['Toyota', 'Daihatsu', 'Honda', 'Suzuki']
print(Mobil) # ['Toyota', 'Daihatsu', 'Honda', 'Suzuki']
print(type (Mobil)) # Hasil masih list
Kendaraan =''.join(Mobil)
print(Kendaraan) # Hasilnya ToyotaDaihatsuHondaSuzuki
print(type (Kendaraan)) # Hasilnya menjadi string

# section 7 : Menunjukkan angka berapa kali muncul
Nilai = [50,52,50,60,68,60,78,70,70,70,72,74,77,72,78,72,72]
print(Nilai.count(50)) # Nilai 50 sebanyak 2
print(Nilai.count(52)) # Nilai 52 sebanyak 1
print(Nilai.count(60)) # Nilai 60 sebanyak 2
print(Nilai.count(70)) # Nilai 70 sebanyak 3
print(Nilai.count(72)) # Nilai 72 sebanyak 4
print(Nilai.count(74)) # Nilai 74 sebanyak 1
print(Nilai.count(77)) # Nilai 77 sebanyak 1
print(Nilai.count(78)) # Nilai 78 sebanyak 2

# section 8 : Membuat kalimat menjadi Besar ataupun Kecil
Jurusan = "Teknik Elektro"
Jurusan2 = "TEKNIK ELEKTRO"
print(Jurusan.lower()) # teknik elektro
print(Jurusan.upper()) # TEKNIK ELEKTRO
print(Jurusan.capitalize()) # Teknik elektro
print(Jurusan2.capitalize()) # Teknik elektro
print(Jurusan2.lower()) # teknik elektro
print(Jurusan2.upper()) # TEKNIK ELEKTRO

# section 9 : 
Hari = ['rabu', 'kamis', 'jumat', 'sabtu']
Jadwal = map(str.upper, Hari)
print(list(Jadwal)) 

# section 10 : Dictionary
Biodata = {"ID":404,
           "Nama": "Leonardo Star Berutu",
           "Pekerjaan":"Mahasiswa",
           "Nim":"190402155"
           "Universitas Sumatera Utara"
            }
print(Biodata)



