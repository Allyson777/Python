from os import system, name

def limpaTela():      
    if name == 'nt':  # Windows
        system('cls')
    else:  # Linux ou outro SO
        system('clear')
def leValor(funcaoConv, msg = ""):
    try:
        return funcaoConv(input(msg))
    except:
        print("ERRO: Tipo inválido")
        return leValor(funcaoConv, msg)

def welcome():
    '''
    FUNÇÃO DE EXIBIÇÃO NO INICIO. 
    '''
    limpaTela()
    print("$--------------------$\n|SEJA BEM-VINDO THUCO|\n$--------------------$")
    _ = input("--> ENTER PARA CONTINUAR...")

def fin(p1,p2,p3,p4,p5):
    '''
    FUNÇÃO DE EXIBIÇÃO AO FINALIZAR O PROGRAMA, ONDE RECEBE COMO PARAMETRO OS 5 PRODUTOS E MOSTRA QUANTOS FORAM VENDIDOS.
    '''
    limpaTela() 
    print("OBRIGADO PELA COMPRA, VOLTE SEMPRE THUTHUCO!")
    print("----------------------------------")
    print(f"FORAM VENDIDOS: {5-p1} X-PARAMETRO")
    print(f"FORAM VENDIDOS: {5-p2} PYTHONXINHA")
    print(f"FORAM VENDIDOS: {5-p3} JUNINHO")
    print(f"FORAM VENDIDOS: {5-p4} X-MINIEP")
    print(f"FORAM VENDIDOS: {5-p5} COCA-RETORNAVEL")

    x1 = faturamento("X-PARAMETRO",p1)
    x2 = faturamento("PYTHONXINHA",p2)
    x3 = faturamento("JUNINHO",p3)
    x4 =  faturamento("X-MINIEP",p4)
    x5 = faturamento("COCA-RETORNAVEL",p5)
    xtotal = x1 + x2 + x3+ x4+x5
    print("----------------------------------")
    print(f"FATURAMENTO TOTAL DO THUCO: R${xtotal:0.2f}")
    exit()
def produtos(p1=5,p2=5,p3=5,p4=5,p5=5):
    """
    Função principal, esta função tem como parametro 5 variaveis onde,cada variavel possui a quantidade que cada produto tem. ex:p1=pythonxinha (5).
    printa a tela principal..
    Exibe o produto e quantidade ao lado, caso a quantidade do produto seja maior que (0).
    Caso a quantidade de produtos for (0) a mensagem de produto esgotado será exibida.
    Se o produto tiver a quantidade maior que 0, cada vez que for selecionado seu número na maquina, será retirado 1
    de sua quantia na variavel, após isso, a maquina ira receber seu pagamento e dar seu troco, tudo calculado pela função (pagamento).
    Após entrega do troco, a função pagamento vaí chamar outra função para exibir se voce deseja comprar novamente
    caso queira, a maquina retornará para o inicio, caso contrario a função (fin) será iniciada e a maquina finalizada. obs: tudo isso se engloba para p1,p2,p3,p4 e p5.
    se o produto tiver a quatidade igual a zero, uma mensagem será exibida, para saber se voce deseja comprar outro produto,
    também possui a variavel (info) caso queira ver informações interna da maquina, estoque e faturamento.
    e por ultimo uma variavel (fim) para encerrar a maquina, nela será exibida quantos produtos foram vendidos e qual foi o faturamento da máquina.
    """
    print ("$-----------LOJA DO THUTHUCO-------------$")    
        #produto1
    produto1= "|1- X-PARAMETRO------------------R$7.50 {}|".format(p1)
    precop1=7.50
        #produto2
    produto2= "|2- PYTHONXINHA------------------R$5.00 {}|".format(p2)
    precop2=5.00
        #produto3
    produto3= "|3- JUNINHO----------------------R$4.50 {}|".format(p3)
    precop3=4.50 
        #produto4
    produto4= "|4- X-MINIEP---------------------R$9.75 {}|".format(p4)
    precop4=9.75
        #produto5
    produto5= "|5- COCA-RETORNAVEL--------------R$3.00 {}|".format(p5)
    precop5=3.00
    info=("|6- Informações Internas                 |")
    fim=("|7- Encerrar sessão                      |")
    print(produto1)if p1>0 else print("PRODUTO ESGOSTADO")     
    print(produto2)if p2>0 else print("PRODUTO ESGOSTADO")
    print(produto3)if p3>0 else print("PRODUTO ESGOSTADO")
    print(produto4)if p4>0 else print("PRODUTO ESGOSTADO")
    print(produto5)if p5>0 else print("PRODUTO ESGOSTADO")
    if p1==0 and p2== 0 and p3 == 0 and p4==0 and p5==0:
        print("$----------------------------------$\n|UEPA, PARECE QUE VOCÊ ZEROU A LOJA|\n|SE QUERER COMPRAR ALGO MAIS       |\n|VÁ A LOJINHA DA 14                |\n$----------------------------------$")
    print("$-------------OUTRAS OPÇÕES--------------$")
    print(info)
    print(fim)
    print("$----------------------------------------$") 
    pedido=leValor(int,"Escolha uma opção: ")
    if pedido==1:
        if p1>0:
            limpaTela()
            print(f"A opção escolhida foi:\n{produto1}\nPreço: R$7,50")  
            p1-=1
            pagamento(precop1,p1,p2,p3,p4,p5)
            produtos(p1,p2,p3,p4,p5)
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N: ")
            if y == "S" or y == "s":
                produtos(p1,p2,p3,p4,p5)
            elif y == "n" or y == "N":
                fin(p1,p2,p3,p4,p5)  
            else:               
                novamente(p1,p2,p3,p4,p5)                       
    elif pedido==2:
        if p2>0:
            limpaTela()
            print(f"A opção escolhida foi:\n{produto2}\nPreço: R$5,00")
            p2-=1
            pagamento(precop2,p1,p2,p3,p4,p5)
            produtos(p1,p2,p3,p4,p5)
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? s/n: ")
            if y == "S" or y == "s":
                produtos(p1,p2,p3,p4,p5)
            elif y == "n" or y == "N":
                fin(p1,p2,p3,p4,p5)
            else:                
                novamente(p1,p2,p3,p4,p5) 
    elif pedido==3:
        if p3 >0:
            limpaTela()
            print(f"A opção escolhida foi:\n{produto3}\nPreço: R$4,50")
            p3-=1
            pagamento(precop3,p1,p2,p3,p4,p5)
            produtos(p1,p2,p3,p4,p5)
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N: ")
            if y == "S" or y == "s":
                produtos(p1,p2,p3,p4,p5)
            elif y == "n" or y == "N":
                fin(p1,p2,p3,p4,p5)
            else:              
                novamente(p1,p2,p3,p4,p5)   
    elif pedido==4:
        if p4>0:
            limpaTela()
            print(f"A opção escolhida foi:\n{produto4}\nPreço: R$9,75")
            p4-=1
            pagamento(precop4,p1,p2,p3,p4,p5)
            produtos(p1,p2,p3,p4,p5)
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N: ")
            if y == "S" or y == "s":
                produtos(p1,p2,p3,p4,p5)
            elif y == "n" or y == "N":
                fin(p1,p2,p3,p4,p5)
            else:               
                novamente(p1,p2,p3,p4,p5)     
    elif pedido==5:
        if p5>0:
            limpaTela()
            print(f"A opção escolhida foi:\n{produto5}\nPreço: R$3,00")             
            p5-=1
            pagamento(precop5,p1,p2,p3,p4,p5)
            produtos(p1,p2,p3,p4,p5)
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N: ")
            if y == "S" or y == "s":
                produtos(p1,p2,p3,p4,p5)
            elif y == "n" or y == "N":
                fin(p1,p2,p3,p4,p5)
            else:               
                novamente(p1,p2,p3,p4,p5) 
    elif pedido==6:
        limpaTela()
        limpaTela()
        print("$------------------------ESTOQUE--------------------------$")
        print("|1- X-PARAMETRO------- Quantidade disponível em estoque: {}|" .format (p1))
        print("|2- PYTHONXINHA------- Quantidade disponível em estoque: {}|".format (p2))
        print("|3- JUNINHO----------- Quantidade disponível em estoque: {}|".format (p3))
        print("|4- X-MINIEP---------- Quantidade disponível em estoque: {}|".format (p4))
        print("|5- COCA-RETORNAVEL--- Quantidade disponível em estoque: {}|".format (p5))
        print("$----------------------FATURAMENTO------------------------$")
        x1 = faturamento("X-PARAMETRO",p1)
        x2 = faturamento("PYTHONXINHA",p2)
        x3 = faturamento("JUNINHO",p3)
        x4 = faturamento("X-MINIEP",p4)
        x5 = faturamento("COCA-RETORNAVEL",p5)
        xtotal = x1+x2+x3+ x4+x5
        print(f"|FATURAMENTO TOTAL: R${xtotal:0.2f}                                |")
        print("$---------------------------------------------------------$")
        x = input("Deseja algo mais thuthuco? S/N: ")
        if x == "S" or x == "s":
            limpaTela()
            produtos(p1,p2,p3,p4,p5)
        elif x == "n" or x == "N":
            fin(p1,p2,p3,p4,p5)
        else:
            limpaTela()
            print("Opção inválida!")
            produtos(p1,p2,p3,p4,p5)    
    elif pedido==7:
        fin(p1,p2,p3,p4,p5)         
    else:
        limpaTela()
        print("Opção inválida, escolha um número de 1 a 7")
        produtos(p1,p2,p3,p4,p5)

def faturamento(nomeproduto, qt):
        """
        Função de faturamento: essa função tem como parametro o nome do pruduto e sua quantidade.
        caso o nome do produto seja escolhido na função produtos, a maquina irá calcular o valor do produto vezes a quantidade que foi retirada
        da máquina, assim podendo fazer o faturamento total, que será exibido após finalizar a maquina ou quando ver as informações internas.

        """
        valorproduto=0
        if nomeproduto=="X-PARAMETRO":
            valorproduto=7.50
        elif nomeproduto=="PYTHONXINHA":
            valorproduto=5.00
        elif nomeproduto=="JUNINHO":
            valorproduto=4.50
        elif nomeproduto=="X-MINIEP":
            valorproduto=9.75
        elif nomeproduto=="COCA-RETORNAVEL":
            valorproduto=3.00                
        if qt==5:            
            return 0.0
        elif qt==4:         
            return valorproduto
        elif qt==3:          
            return valorproduto * 2
        elif qt==2:   
            return valorproduto * 3
        elif qt==1:    
            return valorproduto*4
        elif qt==0:
            return valorproduto*5
        faturamento(nomeproduto,qt)                           

def novamente(p1,p2,p3,p4,p5):
    """
    Esta função foi criada para comprar novamente, mas com a finalidade de reduzir a replicação de código.
    recebe como parametro as variaveis com a quantidade de produtos de p1,p2,p3,p4 e p5
    para que o python não perca o valor que cada uma ainda tem.
    caso queira continuar comprando, maquina retornará para o inicio, caso não queria continuar,
    a função (fin) será chamada novamente e o progama se encerrará. caso nenhuma das opções seja corretamente marcada
    a função novamente será chamada denovo, ate ser completada corretamente.
    """ 

    a=str(input("Deseja comprar novamente Thuthuco? "))
    if a == "S" or a == "s":
        limpaTela()
        produtos(p1,p2,p3,p4,p5)
    elif a == "n" or a == "N": 
        fin(p1,p2,p3,p4,p5)
    else:
        limpaTela()
        print("Opção inválida")
        novamente(p1,p2,p3,p4,p5)

def pagamento(valor,p1,p2,p3,p4,p5,d=0):
    """
    Função de pagamento que irá receber sua quantia(dinheiro), caso a quantia seja menor que 0, uma mensagem
    de erro será exibida, caso seu pagamento for maior que o valor do produto, a função vai calcular seu troco
    chamar a função(troco) para printar as notas e moedas e retirar o valor do produto para a máquina.
    Após calculado, irá chamar a função (novamente), para saber se você deseja continuar comprando.
    Caso o seu valor inserido for menor que o produto e não for menor que 1 centavo
    a função irá repetir, até que o valor que voce inseriu, seja igual ou maior que o valor do produto. 
    """
    dinheiro=leValor(float,"Faça o pagamento: ")
    d+=dinheiro
    if d < 0.01:
        print("Valor inválido, coloque um valor que seja maior ou igual a 0,01 centavo.")
        pagamento(valor,p1,p2,p3,p4,p5,d)
    elif d >= valor:
        limpaTela()
        trocop1=d-valor    
        troco(trocop1)
        print(f"\nPagamento: R${d:0.2f}")
        print(f"Seu troco: R${trocop1:0.2f}")
        novamente(p1,p2,p3,p4,p5)
        return d
    else:
        limpaTela()
        print("Dinheiro insuficiente para o pagamento, insira o restante do pagamento.")
        return pagamento(valor,p1,p2,p3,p4,p5,d)
         
def troco(x):
    """
    Função que tem como parametro o (x), valor que foi calculado em pagamento
    e será repassado para calcular a quantidade de notas que será dado
    e o valor que será retirado da quantia que você inseriu.
    """
    x += 0.000001   #impedir erro
    if x >=100:
        print("R$100,00")
        return troco(x - 100)
    elif x >=50:
        print("R$50,00")
        return troco (x-50)
    elif x >=20:
        print("R$20,00")
        return troco (x-20)
    elif x>=10:
        print("R$10,00")        
        return troco (x-10)
    elif x>=5:
        print("R$5,00")
        return troco (x-5)
    elif x>=2:
        print("R$2,00")
        return troco (x-2)        
    elif x>=1:
        print("R$1,00")
        return troco (x-1)        
    elif x>=0.50:
        print("R$0.50")
        return troco (x-0.50)
    elif x>=0.25:
        print("R$0.25")
        return troco (x-0.25)
    elif x>=0.10:
        print("R$0.10")
        return troco (x-0.10)
    elif x>=0.05:
        print("R$0.05")    
        return troco (x-0.05)
    elif x>0.01:
        print("R$0,01")
        return troco(x-0.01)
        
def main():
    """
    Função main, para definir o que será chamado de começo
    """
    welcome()
    limpaTela()
    produtos()

main()