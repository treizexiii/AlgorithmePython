def impot(revenu, taux, tranche):
    impot = [0, 0, 0, 0]
    reste = int(revenu)
    k = 0

    while (reste > 0) :
        a = min((tranche[k + 1] - tranche[k]), reste)
        impot[k] = int(a * taux[k] / 100)
        reste = revenu - tranche[k]
        k += 1
    
    return impot

def somme(liste) :
    result = 0

    for item in liste:
        result += item
    
    return result

def pourcent(number1, number2)  :
    return number2 / number1 * 100

impot2020 = impot(30000, [0, 10, 20, 50], [0, 10000, 25000, 50000, 200000])
print (impot2020)
print (somme(impot2020))