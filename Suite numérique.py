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

