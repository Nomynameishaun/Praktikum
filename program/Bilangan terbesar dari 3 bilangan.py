a = int(input("bilangan pertama: "))
b = int(input("bilangan kedua: "))
c = int(input("bilangan ketiga: "))

def terbesar(a, b, c):
    if a == b == c:
        print(f"Semua bilangan bernilai sama {a}")
    else:
        terbesar = max(a, b, c)
        print(f"bilangan yang terbesar adalah: {terbesar}")
        
terbesar(a, b, c)  