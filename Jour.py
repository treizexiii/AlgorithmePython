print("Saisir le jour : ")
d = int (input())
print("Saisir le mois : ")
m = int (input())
print("Saisir l'année : ")
a = int (input())

jour = ['Lundi' , 'Mardi', 'Mercredi', 'Jeudi' , 'Vendredi', 'Samedi', 'Dimanche']
mois = ['Janvier', 'Fevrier', 'Mars', 'Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
mnum = 0
k=0
for k in range(0,11):
    if(m == mois[k]):
        mnum = k

dnum= ((23*mnum)//9) + d + 2 + a - (a//4) +(a//100) + (a//400)

j =jour[dnum%7]

print("Le " + str(d) + " " + str(m) + " " + str(a) + " est un " + str(j))
