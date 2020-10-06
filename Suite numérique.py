n = int(input("Quel terme doit-on calculer?"))
u = 500 #formule du terme général
k = 1
while (k <= n):
    u = u * 1.03
    k = k + 1
print(u)

a = 0
b = 5
for k in range(1,11):
    c = a - b + k
    d = a + b - k
print("C = " , c , " et D = " , d )

u = 500
k = 0
while(u< 2000):
    u = u * 1.03 + 100
    k = k + 1
print (k)

a = 0
for k in range(1,101):
    a += k
print(a)