#exercice 8: ecrire une fct qui cherche un element dans unes matrice puis renvoie sa position <i,j>
x=int(input('enter le nombre de colonnes: '))
y=int(input("entrer le nombre de lignes: "))
A=[]
print('entrer les elements de la matrice:')
for i in range(y):
    ligne=[]
    for j in range(x):
        print("A[%d,%d]"%(i+1,j+1),end="")
        ligne.append(int(input()))
    A.append(ligne)
print(A)
n=int(input("entrer element que vous cherchez: "))
def chercher(n):
    for i in range(y):
        for j in range(x):
            if n==A[i][j]:
                print("n[%d,%d]= "%(i+1,j+1),n)
                print('le % est de position : < %d en lignes > et <%d en colonnes>'%(n,i+1,j+1))