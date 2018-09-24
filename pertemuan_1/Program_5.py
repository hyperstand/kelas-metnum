C={
    "nama":"abdul",
    "umur":"54",
    "tinggi":174.5,
    "alamat":"jalan belok"
}#Dictionary

#Ouput
print C

print  "nama : ",C["nama"]


a=input("Masukan angka pertama :")
b=input("Masukan angka kedua :")

if a < b:
    z = b
    print "A lebih kecil dari B "
elif a==b: #else if
    print "A sama dengan b"
else:
    z=a
    print "A lebih besar dari B"

print "Angka Terbesar Adalah :",z