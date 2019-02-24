def data():
    data=[]
    pilih = "Y"
    while pilih == "Y":
        print("Masukkan Data")
        npm = input("NPM =")
        nama = input("Nama =")
        alamat = input("Alamat =")
        a = data.append([npm,nama,alamat])
        pilih = input("Masukkan Data Lagi ? (Y/N) =")
    return(data)

def caridata(data, cari):
    found=0
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y]==cari:
                print(data[x])
                found=found+1
    if found == 0 :
        print("tidak ditemukan")
            
a = data()
b = input("cari npm =")
caridata(a,b)