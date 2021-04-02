# fonction somme (L : liste[]) entier
# total
# debut
#     total = 0
#     pour chaque element de liste :
#         total =+ element
#     retourner total
# fin

# fonction sommeCoef (matrice)
# totalElement
# debut
# totalElement = 0
#     pour chaque element de la matrice
#         totalElement += fonction somme(element)
#     retourner totalElement
# fin


def somme (liste):
    total=0
    for element in liste:
        total += element
    return total

def sommeCoef (matrice):
    totalElement = 0
    for element in matrice:
        totalElement += somme(element)
    return totalElement

result = sommeCoef([3,4,9,2])
print(result)