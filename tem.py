a,b,c = list(map(int, input().split()))

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
if a**2 == (b**2+c**2):
    print("TRIANGULO RETANGULO")
if a**2>(b**2+c**2):
    print("TRIANGULO OBTUSANGULO")
if a**2<(b**2+c**2):
    print("TRIANGULO ACUTANGULO")
if a==b==c:
    print("TRIANGULO EQUILATERO")
if (a==b and c!=a) or (a==c and b!=a) or (c==b and a!=c):
    print("TRIANGULO ISOSCELES") 