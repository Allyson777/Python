peso=float(input())
idade=int(input())
if idade==16 or idade==17:
	docaut =(input())
saude=(input())
drogas=(input())
doacao=(input())
if doacao=="N":
	ultimadoacao=int(input())
	ultimosdoze=int(input())
sexo=(input())
if sexo=="F":
	gravidez=input()
	amamentando=input()
	if amamentando=="S":
		idadebebe=int(input())
print(f"Peso: {peso}")
print(f"Idade: {idade}")
if (idade==16) or (idade==17):
	print(f"Documento de autorizacao: {docaut}")		 
print(f"Boa saude: {saude}")		
print(f"Uso drogas injetaveis: {drogas}")		
print(f"Primeira doacao: {doacao}")
if doacao == "N":
	print(f"Meses desde ultima doacao: {ultimadoacao}")	
	print(f"Doacoes nos ultimos 12 meses: {ultimosdoze}")
print(f"Sexo biologico: {sexo}")		
if sexo=="F":
	print(f"Gravidez: {gravidez}")
	print(f"Amamentando: {amamentando}")
	if amamentando=="S":
		print(f"Meses bebe: {idadebebe}")
verificacao=True
if peso<50:
	print("Impedimento: abaixo do peso minimo.")
	verificacao= False
if idade < 16:
	print("Impedimento: menor de 16 anos.")
	verificacao=False
if idade>=16 and idade<18:
	if docaut=="N":
		print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
		verificacao= False
if idade>60 and doacao=="S":
	print("Impedimento: maior de 60 anos, primeira doacao.")
	verificacao = False
if idade>69:
	print("Impedimento: maior de 69 anos.")
	verificacao = False
if saude=="N":
	print("Impedimento: nao esta em boa saude.")
	verificacao = False
if drogas=="S":
	print("Impedimento: uso de drogas injetaveis.")
	verificacao = False
if doacao=="N" and sexo=="M"and ultimadoacao <2 :
	print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
	verificacao=False
if doacao=="N" and sexo=="F" and ultimadoacao <3 :
	print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
	verificacao=False
if doacao == "N" and sexo == "M" and ultimosdoze >= 4:
	print("Impedimento: numero maximo de doacoes anuais foi atingido.")
	verificacao=False
if sexo=="F" and doacao== "N" and ultimosdoze >= 3:
	print("Impedimento: numero maximo de doacoes anuais foi atingido.")
	verificacao=False
if sexo== "F" and gravidez == "S":
	print("Impedimento: gravidez.")
	verificacao = False
if sexo == "F" and amamentando == "S" and idadebebe <= 12:
	print("Impedimento: amamentacao.")	
	verificacao = False
if verificacao:
	print("Procure um hemocentro.")