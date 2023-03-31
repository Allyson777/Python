######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP4 - Jogo da Velha
# Nome: Allyson Souza Pina Viana    
# Matrícula: 2022102206
######################################################

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):

    print (f" {p7} | {p8} | {p9} ")
    print ("---+---+---")
    print (f" {p4} | {p5} | {p6} ")
    print ("---+---+---")
    print (f" {p1} | {p2} | {p3} ")


def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    
    entrada=True    

    if p1!= "x" and p1 != "o" and p1 != " ":
        entrada=False
    if p2!= "x" and p2 != "o" and p2 != " ":
        entrada=False   
    if p3!= "x" and p3 != "o" and p3 != " ":
        entrada=False 
    if p4!= "x" and p4 != "o" and p4 != " ":
        entrada=False 
    if p5!= "x" and p5 != "o" and p5 != " ":
        entrada=False
    if p6!= "x" and p6 != "o" and p6 != " ":
        entrada=False 
    if p7!= "x" and p7 != "o" and p7 != " ":
        entrada=False 
    if p8!= "x" and p8 != "o" and p8 != " ":
        entrada=False
    if p9!= "x" and p9 != "o" and p9 != " ": 
        entrada = False
    if entrada == True :
        return True 
    else: 
        return False
               
def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    #Complete o código da função
    somax=0
    somao=0
    
    if p1 == "x": somax +=1    
    if p2 == "x": somax +=1    
    if p3 == "x": somax +=1   
    if p4 == "x": somax +=1   
    if p5 == "x": somax +=1   
    if p6 == "x": somax +=1    
    if p7 == "x": somax +=1   
    if p8 == "x": somax +=1                            
    if p9 == "x": somax +=1
    if p1 == "o": somao +=1   
    if p2 == "o": somao +=1   
    if p3 == "o": somao +=1   
    if p4 == "o": somao +=1  
    if p5 == "o": somao +=1   
    if p6 == "o": somao +=1   
    if p7 == "o": somao +=1   
    if p8 == "o": somao +=1                           
    if p9 == "o": somao +=1
    if (somao-somax) >=2  or (somax-somao) >=2:
        return False
    else:
        return True

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    contajogada = 0
    if p1 == p2 and p2 == p3 and p1 != " ":
        print("O jogador 'x' venceu!") if p2 == "x " else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p4 == p5 and p5 == p6 and p4 != " ":
        print("O jogador 'x' venceu!") if p4 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p7 == p8 and p9 == p9 and p8 != " ":
        print("O jogador 'x' venceu!") if p7 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p1 == p4 and p4 == p7 and p7 != " ":
        print("O jogador 'x' venceu!") if p1 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p2 == p5 and p5 == p8 and p2 != " ":
        print("O jogador 'x' venceu!") if p8 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p3 == p6 and p6 == p9 and p3 != " ":
        print("O jogador 'x' venceu!") if p6 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p7 == p5 and p5 == p3 and p5 != " ":
        print("O jogador 'x' venceu!") if p7 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 
    elif p9 == p5  and p5 == p1 and p9 != " ":
        print("O jogador 'x' venceu!") if p9 == "x" else print("O jogador 'o' venceu!")
        contajogada +=1 

    if contajogada == 0:
        if p1 == " " or p2  == " "  or p3 == " " or p4 == " " or p5 == " " or p6 == " "  or p7 == " " or p8 == " " or p9 == " ":
            print("O jogo nao terminou!") 
        else:
            print("Empate!")
             
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
