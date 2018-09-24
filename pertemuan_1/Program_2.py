import math as m

# print m.log(100)
# print m.log10(1000)
# print m.sqrt(4250)
# print m.cos(m.pi/4)
# print m.exp(25)





#Buat fungsi
def hitung_luas(a,t):
    luas=0.5*a*t
    return luas 

def hitung_luas_2(a,t):
    luas=0.5*a*t
    kell= a + t
    return (luas,kell) #tupple


#Hasil fungsi
alas=input("Masukan Alas :")
tinggi=input("Masukan Tinggi :")
hasil=hitung_luas(alas,tinggi)


print "Hasil Luas Segitiga :",hasil

#muncul 4 angka di belakang koma
print "Hasil Luas Segitiga :%.4f"%(hasil)