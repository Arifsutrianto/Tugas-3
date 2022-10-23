def nilai_terbesar(x):
    nilai = max(x)
    print(nilai)
    
list = []
while True:
    data = input("masukkan Angka: ")
    if data == "stop":
        nilai_terbesar(list)
        break
    else:
        list.append(int(data))