def test():
    return(1,2,3)
# tupple nilai static tidak bisa diubah

(a,b,c)=test()
print a
print b
print c

r=test()
print r

r=(5,6,7)
print r