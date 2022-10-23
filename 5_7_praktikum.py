# 1. program yang menerima dua buah bilangan integer sebagai masukan

nilai1 = int(input('Masukkan nilai pertama: '))
nilai2 = int(input('Masukkan nilai kedua: '))
if nilai1 > nilai2 :
    print('Nilai pertama lebih besar')
else:
    print('Nilai kedua lebih besar')


# 2. modifikasi program nmor 1 dengan menambahkan satu masukan lagi menjadi 3.

nilai1 = int(input('Masukkan nilai pertama: '))
nilai2 = int(input('Masukkan nilai kedua: '))
nilai3 = int(input('Masukkan nilai ketiga: '))
if nilai1 > nilai2 and nilai1 > nilai3:
    print('Nilai pertama lebih besar')
elif nilai2 > nilai1 and nilai2 > nilai3:
    print('Nilai kedua lebih besar')
else:
    print('Nilai ketiga lebih besar')


# 3. program yang menerima masukan tiga buah bilangan integer.

nilai1 = int(input('Masukkan nilai pertama: '))
nilai2 = int(input('Masukkan nilai kedua: '))
nilai3 = int(input('Masukkan nilai ketiga: '))
if nilai1 == nilai2 and nilai2 == nilai1:
    print('Nilai pertama dan kedua sama')
elif nilai1 == nilai3 and nilai3 == nilai1:
    print('Nilai pertama dan ketiga sama')
elif nilai2 == nilai3 and nilai3 == nilai2:
    print('Nilai kedua dan ketiga sama')
else:
    print('tidak ada nilai yang sama')


# 4. program menghitung berat badan ideal seseorang. 

nama = (input('Nama anda   : '))
tinggi = int(input('Tinggi anda : '))
berat_ideal = tinggi - 100
print(f'Saudara {nama}, berat ideal anda adalah {int(berat_ideal)} kg')


# 5. program yang menghitung nilai akhir dan grade mata kuliah pemprograman.

print(('DATA NILAI MAHASISWA').center(100))
print('{:^100}'.format('-'*60))
nama = (input    ('Nama  : ').center(100))
tugas = int(input('Tugas : ').center(100))
uts = int(input  ('UTS   : ').center(100))
uas = int(input  ('UAS   : ').center(100))
nilaiakhir = (tugas * (25/100))+(uts * (35/100))+(uas * (40/100)) 
if nilaiakhir >= 75:
    grade = 'A'
elif nilaiakhir >= 60 and nilaiakhir < 75:
    grade = 'B' 
elif nilaiakhir >= 45 and nilaiakhir < 60:
    grade = 'C'
else :
    grade = 'D'
print(('NILAI AKHIR DAN GRADE').center(100))
print('{:^100}'.format('-'*60))
print('Nama        : %s' %nama)
print(('Nilai akhir : %d' %nilaiakhir).center(100))
print(('Grade       : %s' %grade).center(100))
print('{:^100}'.format('-'*60))
