#Jogo do NIM

def computador_escolhe_jogada(n,m):
        
        if n % (m+1) != 0:
            
            jogada_computador = n % (m+1)
            
            if jogada_computador < 1:
                
                jogada_computador = 1
                print('O computador tirou uma peça')
                resto = n - jogada_computador
                n = resto
                if resto == 0:
                    print ('Fim do jogo! O computador ganhou!')
                    
                else:
                        if resto == 1:
                            print('Agora resta apenas uma peça no tabuleiro')
                            usuario_escolhe_jogada(n,m)
                        else:
                            print('Agora restam apenas',resto,'peças no tabuleiro')
                            usuario_escolhe_jogada(n,m)
            else:
                jogada_computador = n % (m+1)
                if jogada_computador == 1:
                        print('O computador tirou uma peça')
                        resto = n - jogada_computador
                        n = resto
                        if resto == 0:
                            print ('Fim do jogo! O computador ganhou!')
                    
                        else:
                                if resto == 1:
                                    print('Agora resta apenas uma peça no tabuleiro')
                                    usuario_escolhe_jogada(n,m)
                                else:
                                    print('Agora restam apenas',resto,'peças no tabuleiro')
                                    usuario_escolhe_jogada(n,m)
                        
                else:
                        print('O computador tirou',jogada_computador,'peças')
                        resto = n - jogada_computador
                        n = resto
                        if resto == 0:
                                print ('Fim do jogo! O computador ganhou!')
                    
                        else:
                                if resto == 1:
                                        print('Agora resta apenas uma peça no tabuleiro')
                                else:
                                        print('Agora restam apenas',resto,'peças no tabuleiro')
                                        usuario_escolhe_jogada(n,m)
        else:
            if n >= m:
                jogada_computador = m
                if jogada_computador == 1:
                        print('O computador tirou uma peça')
                        resto = n - jogada_computador
                        n = resto
                        if resto == 0:
                            print ('Fim do jogo! O computador ganhou!')
                    
                        else:
                                if resto == 1:
                                    print('Agora resta apenas uma peça no tabuleiro')
                                    usuario_escolhe_jogada(n,m)
                                else:
                                    print('Agora restam apenas',resto,'peças no tabuleiro')
                                    usuario_escolhe_jogada(n,m)
                        
                else:
                        print('O computador tirou',jogada_computador,'peças')
                        resto = n - jogada_computador
                        n = resto
                        if resto == 0:
                                print ('Fim do jogo! O computador ganhou!')
                    
                        else:
                                if resto == 1:
                                        print('Agora resta apenas uma peça no tabuleiro')
                                else:
                                        print('Agora restam apenas',resto,'peças no tabuleiro')
                                        usuario_escolhe_jogada(n,m)
            else:
                jogada_computador = n
                if jogada_computador == 1:
                        print('O computador tirou uma peça')
                        resto = n - jogada_computador
                        n = resto
                        if resto == 0:
                                print ('Fim do jogo! O computador ganhou!')
                    
                        else:
                                if resto == 1:
                                        print('Agora resta apenas uma peça no tabuleiro')
                                        usuario_escolhe_jogada(n,m)
                                else:
                                        print('Agora restam apenas',resto,'peças no tabuleiro')
                                        usuario_escolhe_jogada(n,m)
                        
                else:
                        print('O computador tirou',jogada_computador,'peças')
                        resto = n - jogada_computador
                        n = resto
                        if resto == 0:
                                print ('Fim do jogo! O computador ganhou!')
                    
                        else:
                                if resto == 1:
                                        print('Agora resta apenas uma peça no tabuleiro')
                                        usuario_escolhe_jogada(n,m)
                                else:
                                        print('Agora restam apenas',resto,'peças no tabuleiro')
                                        usuario_escolhe_jogada(n,m)
                                        print ('Fim do jogo! O computador ganhou!')  
         
def usuario_escolhe_jogada(n,m):
        
        jogada_usuario = int(input('Quantas peças você vai tirar?')) 
        while jogada_usuario <= 0 or jogada_usuario > m:
                print('Oops! Jogada inválida! Tende de novo.')
                jogada_usuario = int(input('Quantas peças você vai tirar?'))
                if jogada_usuario == 1:
                        print('Você tirou uma peça.')
                        resto = n - jogada_usuario
                        n = resto
                        if resto == 1:
                                print('Agora resta apenas uma peça no tabuleiro')
                                computador_escolhe_jogada(n,m)
                        else:   
                                print('Agora restam apenas',resto,'peças no tabuleiro')
                                computador_escolhe_jogada(n,m)
                        
                else:
                        print('Você tirou', jogada_usuario,'peças.')
                        resto = n - jogada_usuario
                        n = resto
                        if resto == 1:
                                print('Agora resta apenas uma peça no tabuleiro')
                                computador_escolhe_jogada(n,m)
                        else:   
                                print('Agora restam apenas',resto,'peças no tabuleiro')
                                computador_escolhe_jogada(n,m)
        
        if jogada_usuario > 0 and jogada_usuario <= m:
                if jogada_usuario == 1:
                        print('Você tirou uma peça.')
                        resto = n - jogada_usuario
                        n = resto
                        if resto == 1:
                                print('Agora restam apenas uma peça no tabuleiro')
                                computador_escolhe_jogada(n,m)
                        else:   
                                print('Agora restam apenas',resto,'peças no tabuleiro')
                                computador_escolhe_jogada(n,m)
                else:
                        print('Você tirou', jogada_usuario,'peças.')
                        resto = n - jogada_usuario
                        n = resto
                        
                        if resto == 1:
                                print('Agora resta apenas uma peça no tabuleiro')
                                computador_escolhe_jogada(n,m)
                        else:   
                                print('Agora restam apenas',resto,'peças no tabuleiro')
                                computador_escolhe_jogada(n,m)
                        
                
def partida():
        
        n = int(input('Quantas peças?'))
        m = int(input('Limite de peças por jogada?'))
           
        if n % (m+1) == 0:
                print('Você começa!')
                usuario_escolhe_jogada(n,m)
        
        else:
                print('Computador começa!')
                computador_escolhe_jogada(n,m)
       

       
def campeonato():

        placar_computador = 0
        print('**** Rodada 1 ****')
        partida()
        placar_computador = (placar_computador +1)
        print('**** Rodada 2 ****')
        partida()
        placar_computador = (placar_computador +1)
        print('**** Rodada 3 ****')
        partida()
        placar_computador = (placar_computador +1)
        print('Placar: Você 0 X Computador', placar_computador)
        

   
            
def inicio():
    
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        escolha = int(input(''))

        if escolha == 1:
                print('Você escolheu uma partida isolada!')
                print("")
                partida()
        if escolha == 2:
                print('Você escolheu um campeonato!')
                print("")
                campeonato()
        

        

inicio()


                                 


