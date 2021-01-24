print ("Menghitung Luas Segitiga")

alas = int (input("Masukkan Alas : "))
tinggi = int (input("Masukkan Tinggi : "))


if 0< alas <100 and 0 < tinggi < 100 :

	luas = int (0.5*alas*tinggi)
	print ("Luas Segitiga adalah ",luas)

else :
	print("MASUKKAN ANGKA ANTARA 0 - 100")


while True :
    jawab = str (input("Apakah anda ingin mengulang lagi ?"))
    if jawab == ("Y") :

        alas = int (input("Masukkan Alas : "))
        tinggi = int (input("Masukkan Tinggi : "))


        if 0< alas <100 and 0 < tinggi < 100 :

	        luas = int (0.5*alas*tinggi)
	        print ("Luas Segitiga adalah ",luas)

        else :
	        print("MASUKKAN ANGKA ANTARA 0 - 100")

    elif jawab == ("tidak") :
        print("Terima kasih")
        break

    else :
        print('WARNING !!! masukkan "Y" atau "tidak"')