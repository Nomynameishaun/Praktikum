# Memulai program
bilangan_maksimal = float('-inf')  # Inisialisasi bilangan maksimal dengan negatif tak terhingga

# Input jumlah bilangan yang akan dimasukkan
n = int(input("Masukkan jumlah bilangan: "))

# Loop untuk meminta input bilangan sebanyak 'n' kali
while n > 0:
    bilangan = int(input("Masukkan bilangan: "))
    
    # Mengecek apakah bilangan lebih besar dari bilangan maksimal
    if bilangan > bilangan_maksimal:
        bilangan_maksimal = bilangan  # Update bilangan maksimal
        
    # Mengurangi jumlah iterasi
    n -= 1

# Output bilangan maksimal
print("Bilangan maksimal adalah:", bilangan_maksimal)
