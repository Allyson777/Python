######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP3 - Ironman
# Nome: Allyson Souza Pina Viana
# Matrícula:2022102206
######################################################

def inicio():
    sexo=input()
    idd=int(input())
    nat=int(input())
    natxcic=int(input())
    cic=int(input())
    cicxcorr=int(input())
    corr=int(input())
    temp= nat + natxcic + cic + cicxcorr + corr
    return sexo, idd, temp
def main():
    sexo, idd, temp = inicio()        
    if idd >= 18 and idd <=29: 
        if sexo == "m" or sexo == "M":  
            tempomax1=480 
        else:
            tempomax1=490
    elif idd >= 30 and idd <=34:
        if sexo == "m" or sexo == "M":
            tempomax1= 490
        else:
            tempomax1= 500
    elif idd >= 35 and idd <= 39:
        if sexo == "m" or sexo == "M":
            tempomax1=505
        else:
            tempomax1=520
    elif idd >= 40 and idd <= 44:
        if sexo == "m" or sexo == "M":
            tempomax1=515
        else:
            tempomax1=540
    elif idd >= 45 and idd <= 49:
        if sexo == "m" or sexo == "M":
            tempomax1=530
        else:
            tempomax1= 560
    elif idd >= 50 and idd <= 54:
        if sexo == "m" or sexo == "M":
            tempomax1=540
        else:
            tempomax1=580  
    elif idd >= 55 and idd <=59:
        if sexo == "m" or sexo == "M":
            tempomax1=555  
        else:
            tempomax1=600
    elif idd >=60 and idd <= 64:
        if sexo == "M" or sexo == "m": 
            tempomax1=570
        else:
            tempomax1=630
    elif idd >= 65 and idd <= 69:
        if sexo ==  "M" or sexo == "m":
            tempomax1=590  
        else:
            tempomax1=660
    elif idd >= 70 and idd <= 74:
        if sexo == "m" or sexo == "M":
            tempomax1=620
        else:
            tempomax1=705
    elif idd >= 75 and idd <= 79:
        if sexo == "m" or sexo == "M":
            tempomax1=660
        else:
            tempomax1=750
    elif idd >= 80:
        if sexo == "m" or sexo == "M":
            tempomax1=720
        else:
            tempomax1=810
    if sexo == "M" or sexo =="m":
        print(f"Tempo do atleta: {temp//60:02d}h {temp%60:02d}min")
    else:
        print(f"Tempo da atleta: {temp//60:02d}h {temp%60:02d}min")    
    print(f"Tempo necessario: {tempomax1//60:02d}h {tempomax1%60:02d}min")
    if temp <= tempomax1:
        print("Conseguiu indice? SIM")
    else:
        print("Conseguiu indice? NAO") 
    indice = temp - tempomax1
    if (sexo == "m" or sexo == "M"):
        if indice <=0:
            print(f"O atleta terminou a prova {(indice*(-1))//60:02d}h {(indice*(-1))%60:02d}min abaixo do indice")
        else:
            print(f"O atleta terminou a prova {indice//60:02d}h {indice%60:02d}min acima do indice")
    else:
        if indice <= 0:
            print(f"A atleta terminou a prova {(indice*(-1))//60:02d}h {(indice*(-1))%60:02d}min abaixo do indice")    
        else:
            print(f"A atleta terminou a prova {indice//60:02d}h {indice%60:02d}min acima do indice")    
    

main()    






