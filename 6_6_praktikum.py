

# 2. program yang menampilkan deret geometri

a = float(input('Nilai Awal : '))
un = int(input('Suku akhir : '))
u = int(input('banyaknya suku :'))
r = float(input("Rasio : "))
for n in range(u, un+1):
    suku = a*(r**(n-1))
    print(suku)



# 3. program yang menginput sejumlah N(input)

data_n = input('\nMasukan nilai N, pisahkan dengan tanda koma. contoh: 1,2,3,dst : ')
list_angka = data_n.split(',')
daftar_baru = [int(x) for x in list_angka]
jumlah = 0
for angka in daftar_baru:
    jumlah += angka
rata_rata = jumlah / len(daftar_baru)
print('\nJumlah  total: {}'.format(jumlah))
print(f'Nilai rata-rata: {int(rata_rata)}')



# 4. buatlah program menghitung X^y dengan x bilangan real dan y bilangan bulat positif

print(('\nAplikasi perhitungan berpangkat dengan posisi X^y'))
x = int(input('Masukan nilai x : '))
y = int(input('Masukan nilai y : '))
hasil = x ** y
print(f'\nHasil = {hasil}')



# 5. program menghitung N! dengan N sebagai masukan

x = int(input('Masukkan nilai n: '))
faktorial = 1
for i in range(1, x + 1):
  faktorial *= i
print(f'{x}! = {faktorial}')



# 6. program tebak angka dimana pengguna menginput suatu bilangan integer antara 0-10 yang telah diacak komputer.

import random
nilacak = random.randint(0, 10)
print('Coba tebak angka saya, dari 0-10')
print('=' *50)
while True:
  tebakan = int(input('\nMasukkan angka: '))
  if tebakan == nilacak:
    print('Tebakanmu benar!')
    break # berhenti paksa
  else:
    print(
      'Angka tebakan lebih',
      'kecil' if tebakan < nilacak else 'besar')



# 7. program untuk menampilkan dan menjumlahkan semua bilangan antara nilai X dan Y 

print('Masukan angka X dan Y untuk menghitung jumlah angka dari X sampai Y')
print('=' *50)
x= int(input('Masukan nilai X   : '))
y= int(input('Masukan nilai Y   : '))
print('Deret    : ')
for antara in range(x,y+1):
    print(antara, end=' ')
jumlah= sum(range(x,y+1))
print(f'\nJumlah : {jumlah}')


# 8. program menampilkan bentuk perulangan

#a. Masukkan N=5
s = '  '
for n in range (6):
    if (n != 0):
        s += str (n)+'  '
print (s)

s = '  '
for n in range (6,11):
    s += str (n)+'  '
print (s)

s = ' '
for n in range (11,16):
    s += str (n)+' '
print (s)


# c. masukkan N=5
n = int(input("Masukkan angka: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end='')
        
    print()
    n-=1
    
# d. Masukkan N=4

s = ' '
for n in range (5):
    if (n != 0):
        s += str (n)+' '
print (s)

s = ' '
for n in range (5,9):
    s += str (n)+' '
print (s)

s = ' '
for n in range (9,13):
    s += str (n)+' '
print (s)