def persegipanjang():
    print("Menghitung luas Persegi Panjang")
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
    luas = (panjang*lebar)
    print("Luas Persegi Panjang adalah: ",luas,"cm")
    
persegipanjang()

def lingkaran():
    print("Menghitung luas Lingkaran")
    r = int(input("Masukkan nilai jari-jari lingkaran: "))
    luas = (22/7*r*r)
    print("Luas Lingkaran adalah: ",luas,"cm")
    
lingkaran()

def segitiga():
    print("Menghitung luas segitiga")
    alas = int(input("Masukkan nilai alas: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    luas = (alas*tinggi/2)
    print("Luas segitiga adalah: ",luas,"cm")
    
segitiga()