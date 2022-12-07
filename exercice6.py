#exercice 6: ecrire une fonction en python pour compter les chiffres d'un nombre donné
x=input('entrer un nombre: ')
def chiffre(x):
    b=0
    for a in range (len(x)):
        b+=1
    return b

print("le chiffre du nbre" ,x," est:" ,chiffre(x))
