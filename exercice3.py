#exercice3: ecrire une fct en Python pour trouver la somme des series 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 en utilisant la fonction
x= int(input("entre un nbre: "))
def factoriel (x):
    b=1
    for a in range (1,x+1):
        b=a*b
    return b
def somme_serie(a):
    b=0
    for a in range (1,x+1):
        b+=factoriel(a)/a
    return b
print("la somme de la serie est :" ,somme_serie(5))
