#ecrire une fonction en python pour convertir le nbre decimal en binaire
list=[]
a=int(input("entrer un nbre: "))
n=a
def binaire (a):
    while(a>0):
        i=0
        list.insert(i,a%2)
        a=a//2
        i+=1
    for i in range (len(list)):
        print(list[i],end='')
    return list
print("le nombre binaire du nombre decimal %d est: " %a,end= '')
binaire (a)