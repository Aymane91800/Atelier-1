#exercice5: ecrire une fonction en python pour compter les chiffres d'un nombre donné.
x=int(input("entrer un nombre: "))
def somme(x):
    b=0
    for a in range (x+1):
        b+=a
    return b
print("la somme des nbres de 1 à %d est: "%x,somme(x))
