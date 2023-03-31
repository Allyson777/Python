def entrada(n, lista=[], listavotos=[ ],i=1):
    if i <= n:
        candidatos=input()
        lista+=[candidatos]
        listavotos+=[0]
        return entrada(n, lista, listavotos, i+1)
    else:
        pessoas=int(input()) 
        lista+=["Nulos"]
        listavotos+=[0]
        return votos(n,pessoas, lista, listavotos)
       
def votos(n, pessoas, lista=[ ], listavotos=[ ],i=0):
    
    if i < pessoas:
        votoscand=int(input())
        if votoscand == 0:
            listavotos[votoscand]+=1
            return votos(n, pessoas, lista,listavotos, i+1)
        elif votoscand <= n:
            listavotos[votoscand]+=1
            return votos(n, pessoas, lista,listavotos, i+1)
        elif votoscand > n:
            listavotos[n+1]+=1
            return votos(n, pessoas, lista,listavotos, i+1)
    else:
        resultado(n,pessoas, lista, listavotos)       

def resultado(n,pessoas,lista=[], listavotos=[ ],i=1):
    if i < len(lista)-1:
        print(f"{lista[i]}: {listavotos[i]}")
        return resultado(n,pessoas,lista, listavotos,i+1)             
    else:
        print(f"Brancos: {listavotos[0]}")
        print(f"Nulos: {listavotos[n+1]}")
        return ganhador(n,pessoas,lista, listavotos)

def ganhador(n,pessoas,lista=[], listavotos=[ ],i=1,maior=1):
    if i<len(lista)-1:
        if listavotos[i]>listavotos[maior]:
            maior=i
        return ganhador(n,pessoas,lista, listavotos,i+1,maior)    
    else:    
        print(f"Vencedor(a): {lista[maior]}")

def main():
    n=int(input())
    entrada(n,lista=["Brancos"], listavotos=[0],i=1)
    
main()    