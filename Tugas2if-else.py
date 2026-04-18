# soal:
# masukan nama anda ;{nama pendek anda}
# jika benar akan lanjut ke program selanjutnya
# jika salah, akan muncul pesan "silahkan coba lagi"

# buat program yang menampilkan tabel perkalian dari angka yang di masukan user (1,50).
# contoh:
# masukan angka:3 
# 3 x 1= 3
# 3 x 2= 6
# ...
# 3 x 1= 30

# jawab :

nama= input ("masukan nama pendek anda")

if nama== "yogi":
    print("Thankyou telah memasukkan nama anda yg keren")
    print("Ayo lanjut ke programan berikutnya")
    
else:
    print("mohon maaf nama yang anda masukan salah")
    print("silahkan coba lagi")

angka= int (input("mau Lihat perkalian kilat? Silahkan masukkan angka yg mau dikalikan"))

for i in range (1,11):
    hasil= angka*i
    print(f"{angka}*{i}={hasil}")

print ("Thankyou program selesai")