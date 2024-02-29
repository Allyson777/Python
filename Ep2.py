######################################################
# Programação Funcional / Programção I (2022/2)
# EP2 - Jogo da Velha
# Nome: Allyson Souza Pina Viana
# Matrícula: 2022102206
######################################################
import random
from os import system, name

def limpaTela():      
    if name == 'nt':  # Windows
        system('cls')
    else:  # Linux ou outro SO
        system('clear')

def leValor(funcaoConv, msg=""):
    try:
        return funcaoConv(input(msg))
    except:
        print("\033[1;31;107m#ERRO: Tipo inválido\033[m")
        return leValor(funcaoConv, msg)

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "MATRICULA: 2022102206"

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "ALUNO: ALLYSON SOUZA PINA VIANA "

def inicio():
    '''
    FUNÇÃO DE EXIBIÇÃO NO INICIO.
    '''
    limpaTela()
    print("\033[7;96;107mSEJA BEM-VINDO AO JOGO DA VELHA|\n\033[m")
    _ = input("\033[7;96;107m--> ENTER PARA COMEÇAR JOGAR...\033[m")

def imprimeTabuleiro(l):
    """
    FUNÇÃO PARA IMPRIMIR O TABULEIRO
    PARAMETRO: (l) LISTA DE TAMANHO 10 REPRESENTANDO O TABULEIRO. 
    """
    print(f'\033[7;31;107m===================================================\033[m')
    print('\033[1;31;40m#                       VELHA                     #\033[m')
    print('\033[7;31;107m===================================================\033[m')
    print("\033[1;31;107m __________________________________________________\033[m")  
    print("\033[1;31;107m|        _____________________________            |\033[m")  
    print("\033[1;31;107m| == .  |        ┌───┬───┬───┐        |     o     |\033[m")  
    print(f"\033[1;31;107m|   _   |        | {l[7]} | {l[8]} | {l[9]} |        |    B      |\033[m")  
    print("\033[1;31;107m|  / \  |        ├───┼───┼───┤        | A   O     |\033[m")  
    print(f"\033[1;31;107m| | O | |        | {l[4]} | {l[5]} | {l[6]} |        |  O        |\033[m")  
    print("\033[1;31;107m|  \_/  |        ├───┼───┼───┤        |           |\033[m")  
    print(f"\033[1;31;107m|       |        | {l[1]} | {l[2]} | {l[3]} |        | . . .     |\033[m")  
    print("\033[1;31;107m|  :::  |        └───┴───┴───┘        | . . .     |\033[m")  
    print("\033[1;31;107m|  :::  |_____________________________| . . .     |\033[m")  
    print("\033[1;31;107m|                A L L Y S O N                    |\033[m")
    print("\033[1;31;107m|_________________________________________________|\033[m")

def escolhajogador():
    """
    FUNÇÃO PARA ESCOLHA DE SIMBOLO DO JOGADOR PARA O GAME, ENTRE X OU O, E RETORNA QUAL FOI ESCOLHIDO.
    """
    limpaTela()
    escolha = input(("\033[7;31;107mVOCÊ DESEJA JOGAR COM QUAL SIMBOLO: (X) OU (O)\033[m"))

    if escolha == "X" or escolha == "x":
        limpaTela()
        print(f"\033[7;49;91mVOCÊ JOGARÁ COM ({escolha}) E O COMPUTADOR COM (O)\033[m")
        simbolojogador = "X"
        simbolocomputador = "O"
        return simbolocomputador, simbolojogador
    elif escolha == "O" or escolha == "o":
        limpaTela()
        print(f"\033[1;31;107mVOCÊ JOGARÁ COM({escolha}) E O COMPUTADOR COM (X)\033[m")
        simbolojogador = "O"
        simbolocomputador = "X"
        return simbolocomputador, simbolojogador
    else:
        limpaTela()
        print("\033[1;31;107mOPÇÃO INVALIDA\033[m")
        return escolhajogador()

def primeirojogador(pc, player):
    """
    FUNÇÃO PARA DEFINIR QUEM IRA JOGAR PRIMEIRO, COM UMA ESCOLHA ALEATORIA DO MODO RANDOM.CHOICE
    E RETORNA QUEM IRÁ FAZER A PRIMEIRA JOGADA.
    PARAMETROS: (PC) É O COMPUTADOR. (PLAYER) O JOGADOR EM PESSOA.
    """
    one = [pc, player]
    one = random.choice(one)
    if one == "X" or one == "x":
        print("                  \033[1;31;40mJOGADOR X COMEÇA\033[m")
        return one
    elif one == "O" or "o":
        print("                  \033[1;31;40mJOGADOR O COMEÇA\033[m")
        return one

def jogjogador(l):
    """
    FUNÇÃO PARA O JOGADOR ESCOLHER A POSIÇÃO QUE DESEJA JOGAR, VERIFICA SE É VÁLIDA 
    E RETORNA A POSIÇÃO DESEJADA.
    PARAMETRO: (l) LISTA DE TAMANHO 10 REPRESENTANDO O TABULEIRO. 
    """
    jogada = leValor(int, "\033[7;31;107mQUAL POSIÇÃO VOCÊ VAI JOGAR: \033[m ")

    if jogada <= 0 or jogada >= 10:
        limpaTela()
        print("\033[7;31;107mPOSIÇÃO INVALIDA, TENTE NOVAMENTE:\033[m ")
        imprimeTabuleiro(l)
        return jogjogador(l)
    elif l[jogada] != " ":
        limpaTela()
        print("\033[7;31;107mPOSIÇÃO PREENCHIDA, ESCOLHA OUTRA:\033[m ")
        imprimeTabuleiro(l)
        return jogjogador(l)
    else:
        return jogada

def verificajogada(tabuleiro,simboloS,simboloJogador,defesa=1):
    """
    FUNÇÃO PARA VERIFICAR A JOGADA DO JOGADOR, SEJA ELE COMPUTADOR OU PLAYER
    E FAZER UMA DEFESA OU ATAQUE, DEPEDENDO DE QUEM ESTIVER JOGANDO E DAS CONDIÇÕES DE JOGO.
    PARAMETROS:(TABULEIRO)LISTA DE TAMANHO 10 REPRESENTANDO O TABULEIRO.
    (SIMBOLO) E (SIMBOLOJOGADOR) PARA VERIFICAR OS SIMBOLOS QUE POSSAM FECHAR A PARTIDA.
    (defesa=1) PARA FAZER A PROXIMA VERIFICAÇÃO QUANDO ALGUM "IF" NÃO É VALIDO.   
    """    
    if defesa <= 7:
        if defesa == 3 or defesa == 1:
            if tabuleiro [defesa] == simboloS and tabuleiro [5] == simboloS and tabuleiro [10-defesa] == " " :
                return 10 - defesa
            elif tabuleiro [5] == simboloS and tabuleiro [10-defesa] == simboloS and tabuleiro [defesa] == " " :
                return defesa
            elif tabuleiro [defesa] == simboloS and tabuleiro [10-defesa] == simboloS and tabuleiro [5] == " " :
                return 5
        if defesa == 7 or defesa == 1 or defesa == 4:
            if tabuleiro [defesa] == simboloS and tabuleiro [defesa+1] == simboloS and tabuleiro [defesa+2] == " " :
                return defesa + 2
            elif tabuleiro [defesa] == simboloS and tabuleiro [defesa+2] == simboloS and tabuleiro [defesa+1] == " " :
                return defesa + 1
            elif tabuleiro [defesa+1] == simboloS and tabuleiro [defesa+2] == simboloS and tabuleiro [defesa] == " " :
                return defesa
        if defesa == 3 or defesa == 2 or defesa == 1:
            if tabuleiro [defesa] == simboloS and tabuleiro [defesa+3] == simboloS and tabuleiro [defesa+6] == " " :
                return defesa + 6
            elif tabuleiro [defesa + 3] == simboloS and tabuleiro [defesa + 6] == simboloS and tabuleiro [defesa] == " " :
                return defesa
            elif tabuleiro [defesa] == simboloS and tabuleiro [defesa + 6] == simboloS and tabuleiro [defesa + 3] == " " :
                return defesa + 3            
                    
        return verificajogada(tabuleiro,simboloS,simboloJogador,defesa+1)
    else:
        if simboloS == simboloJogador:
            return 0
        else:
            return verificajogada(tabuleiro,simboloJogador,simboloJogador,defesa=1)

def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas,
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador
    Retorno:
    Posição (entre 1 e 9) da jogada do computador
    """
    simboloJogador = "X" if simboloComputador == "O" else "O"
    defesa = verificajogada(tabuleiro,simboloComputador,simboloJogador)
    if defesa!=0:
        return defesa    
    elif tabuleiro [5] == " ":
        return 5  
    elif tabuleiro [1] == simboloJogador and tabuleiro [6] == simboloJogador and tabuleiro [8] == simboloJogador and tabuleiro [9] == " ":   
        return 9
    elif tabuleiro [3] == simboloJogador and tabuleiro [4] == simboloJogador and tabuleiro [8] == simboloJogador and tabuleiro [7] == " ":
        return 7
    elif tabuleiro [4] == simboloJogador and tabuleiro [8] == simboloJogador and tabuleiro [7] == " ":
        return 7     
    elif tabuleiro [4] == simboloJogador and tabuleiro [2] == simboloJogador and tabuleiro [1] == " ":
        return 1    
    elif tabuleiro [6] == simboloJogador and tabuleiro [2] == simboloJogador and tabuleiro [3] == " ":
        return 3
    elif tabuleiro [6] == simboloJogador and tabuleiro [8] == simboloJogador and tabuleiro [7] == " ":
        return 7 
    elif tabuleiro [1] == simboloJogador and tabuleiro [8] == simboloJogador and tabuleiro [7] == " ":
        return 7 
    elif tabuleiro [3] == simboloJogador and tabuleiro [8] == simboloJogador and tabuleiro [9] == " ":
        return 9                                
    elif tabuleiro [5] == simboloJogador and tabuleiro [1] == " ":
        return 1
    elif tabuleiro [5] == simboloJogador and tabuleiro [3] == " ":
        return 3
    elif tabuleiro [5] == simboloJogador and tabuleiro [7] == " ":
        return 7
    elif tabuleiro [5] == simboloJogador and tabuleiro [9] == " ":        
        return 9  
    elif tabuleiro[2] == " " :
        return 2
    elif tabuleiro [6]== " ":   
        return 6
    elif tabuleiro[8] == " " :
        return 8 
    elif tabuleiro[4] == " " :
        return 4         
    elif tabuleiro [1] == " ":
        return 1     
    elif tabuleiro [9] == " ":
        return 9 
    elif tabuleiro [3] == " ":
        return 3
    elif tabuleiro [7] == " ":
        return 7                      

def imprimejogada(simbolojogador, simbolocomputador, jogada, tabuleiro):
    """
    FUNÇÃO PARA IMPRIMIR A JOGADA DO COMPUTADOR E DO JOGADOR
    VERIFICANDO DE QUEM É A VEZ DE JOGAR, APÓS ISSO, A MESMA IMPRIME O TABULEIRO
    COM A JOGADA DO JOGADOR OU DO COMPUTADOR E CHAMA A FUNÇÃO (VERIFICA), PARA
    VERIFICAR SE JÁ TEM ALGUM GANHADOR E RETORNA (IMPRIMEJOGADA), MAS AGORA COM UMA DIFERENÇA
    O PARAMETRO (JOGADA) IRÁ SER ALTERADO PARA O PRÓXIMO JOGADOR, ASSIM EVITANDO DE CAIR EM UM LOOP.
    PARAMETROS: (SIMBOLOJOGADOR) E (SIMBOLOCOMPUTADOR) SÃO OS SIMBOLOS DE CADA JOGADOR.
    (JOGADA) VERIFICA DE QUEM É A VEZ DE JOGAR.
    (TABULEIRO) O PRÓPIO TABULEIRO COM AS POSIÇÕES PRENCHIDAS E VAZIAS A CADA JOGADA
    
    """
    if jogada == simbolojogador:
        imprimeTabuleiro(tabuleiro)
        primeiraj = jogjogador(tabuleiro)
        tabuleiro[primeiraj] = simbolojogador
        verifica(tabuleiro,jogada)
        return imprimejogada(simbolojogador, simbolocomputador,simbolocomputador, tabuleiro)
    elif jogada == simbolocomputador:
        primeirajpc = jogadaComputador(tabuleiro, simbolocomputador)
        tabuleiro[primeirajpc] = simbolocomputador
        verifica(tabuleiro,jogada)
        return imprimejogada(simbolojogador, simbolocomputador, simbolojogador,tabuleiro)

def verifica(l, simbolo):
    """
    FUNÇÃO PARA VERIFICAR O GANHADOR DA PARTIDA OU SE DEU EMPATE
    DE ACORDO COM AS REGRAS DO JOGO DA VELHA
    PARAMETROS:(L) (l) LISTA DE TAMANHO 10 REPRESENTANDO O TABULEIRO. (SIMBOLO) SIMBOLO DO COMPUTADOR OU JOGADOR.
    """
    if l[1] == l[2] and l[2] == l[3] and l[1] != " ":
        ganhador(l,simbolo)
    elif l[4] == l[5] and l[5] == l[6] and l[4]!= " ":    
        ganhador(l,simbolo,)
    elif l[7] == l[8] and l[8] == l[9] and l[8]!= " ":   
        ganhador(l,simbolo)
    elif l[1] == l[4] and l[4] == l[7] and l[7]!= " ":     
        ganhador(l,simbolo)
    elif l[2] == l[5] and l[5] == l[8] and l[2]!= " ":    
        ganhador(l,simbolo)
    elif l[3] == l[6] and l[6] == l[9] and l[6]!= " ":    
        ganhador(l,simbolo)
    elif l[7] == l[5] and l[5] == l[3] and l[3]!= " ":       
        ganhador(l,simbolo)
    elif l[9] == l[5] and l[5] == l[1] and l[5]!= " ":      
        ganhador(l,simbolo)
    elif l[1] != " " and l[2] != " " and l[3] != " " and l[4] != " " and l[5] != " " and l[6] != " " and l[7] != " " and l[8] != " " and l[9] != " ":
        limpaTela()
        print("\033[7;31;107m                       DEU VELHA                   \033[m")
        imprimeTabuleiro(l)
        deseja=input("\033[7;31;107mDESEJA TENTAR NOVAMENTE?:(S) OU ( )          \033[m")
        if deseja== "s" or deseja == "S":         
            main()           
        else:
            limpaTela()
            print("\033[7;31;107mNÃO CONSEGUE NÉ? TENTE NOVAMENTE MAIS TARDE.\033[m")
            exit()        

def ganhador(lista,simbolos):
    """
    COMPLEMENTO DA FUNÇÃO GANHADOR, PARA EVITAR REPLICAÇÃO DE CÓDIGO. 
    VERIFICA QUAL SIMBOLO É O VENCEDOR E IMPRIME O TABULEIRO
    PARAMETROS:(LISTA) (l) LISTA DE TAMANHO 10 REPRESENTANDO O TABULEIRO.  (SIMBOLO) SIMBOLO DO COMPUTADOR OU JOGADOR.
    """
    limpaTela()
    print(f"\033[1;31;40mO JOGADOR {simbolos} É O VENCEDOR\033[m")
    imprimeTabuleiro(lista)   
    deseja=input("\033[7;31;107mDESEJA JOGAR NOVAMENTE, PATO?:(S) OU ( )\033[m")
    if deseja== "s" or deseja == "S":
        main()
    else:
        limpaTela()
        print("\033[7;31mFOI BOM GANHAR DE VOCÊ, TENTE NOVAMENTE MAIS TARDE.\033[m")
        exit()        

def main():
    """
    FUNÇÃO PRINCIPAL, TEM UMA LISTA COM 10 POSIÇÕES E INICIA O JOGO. FAZ A FUNÇÃO ESCOLHA JOGADOR RECEBER UM SIMBOLO
    VERIFICA A VARIAVEL (ONE) PARA VER QUEM IRÁ COMEÇAR, E IMPRIME A JOGADA NO TABULEIRO, COM A FUNÇAO (IMPRIME JOGADA)
    """
    l = [" "] * 10
    inicio()
    simbolocomputador, simbolojogador = escolhajogador()
    one = primeirojogador(simbolocomputador, simbolojogador)
    imprimejogada(simbolojogador, simbolocomputador, one, l)
    # print(getNome())
    # print(getMatricula())
################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()