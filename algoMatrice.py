def saisie():
    m = int(input('Saisir le nombre de lignes'))
    n = int(input('Saisir le nombre de colonnes'))
    M=[[0]*n]*m
    for i in range (0,m):
        for j in range(0,n):
            M[i][j]=(input('Saisir le coefficient à la place ' + str(i) + ' ' + str(j)))
    return M

print(saisie())