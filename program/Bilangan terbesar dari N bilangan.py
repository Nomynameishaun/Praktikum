bilangan_maksimal = float('-inf')  
n = int(input("Masukkan jumlah bilangan: "))

while n > 0:
    bilangan = int(input("Masukkan bilangan: "))
    
    if bilangan > bilangan_maksimal:
        bilangan_maksimal = bilangan
        
    n -= 1

print("Bilangan maksimal adalah:", bilangan_maksimal)
