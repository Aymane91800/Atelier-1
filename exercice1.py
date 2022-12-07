#Ecrire une fonction qui renvoie la puissance d'un nombre Xn
X=int(input('entrer un nombre: '))
n=int(input('entrer la puissance: '))
def puissance(X,n):
    X*=X
    return X

print('le resultat du nbre %d à la puissance %d est: '%(X,n),puissance(X,n))
