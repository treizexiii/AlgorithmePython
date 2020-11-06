def tri(laListe):
    i = 0
    j = 0
    temp = 0
    longueur = len(laListe)
    for i in range(0, (longueur-1)):
        for j in range(i+1, longueur):
            if(laListe[i] > laListe[j]):
                temp = laListe[i]
                laListe[i] = laListe[j]
                laListe[j] = temp
    print(laListe)



