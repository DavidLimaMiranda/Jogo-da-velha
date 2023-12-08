
from tkinter import *


# cores usadas

branco = "#FFFFFF"  # branca / white
preto = "#171716"  # preta um pouco mais claro / dark black
azul = "#3297a8"   # azul / blue 
amarelo = "#fff873"   # amarela / yellow
laranja = "#fcc058"  # laranja / orange
vermelho = "#e85151"   # vermelha / red
preto = "#000000" # preta / black 


# Criando a janela com o tkinter

janela = Tk()
janela.title('Jogo da velha')
janela.geometry('800x700')
janela.configure(bg=preto)


# Dividindo os frames da janela

frame_cima = Frame(janela, width=780, height=120, bg=preto, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=780, height=580, bg=preto, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)


# Configurando o frame de cima

# Jogador X

app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font='arial 50 bold', bg=preto, fg=vermelho)
app_x.place(x=235, y=0)

app_x = Label(frame_cima, text='Jogador X', height=1, relief='flat', anchor='center', font='arial 15 bold', bg=preto, fg=vermelho)
app_x.place(x=210, y=70)

labelPontosX = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font='arial 40 bold', bg=preto, fg=branco)
labelPontosX.place(x=325, y=20)

# Jogador O

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font='arial 50 bold', bg=preto, fg=azul)
app_o.place(x=500, y=0)

app_o = Label(frame_cima, text='Jogador O', height=1, relief='flat', anchor='center', font='arial 15 bold', bg=preto, fg=azul)
app_o.place(x=480, y=70)

labelPontosO = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font='arial 40 bold', bg=preto, fg=branco)
labelPontosO.place(x=430, y=20)


# Separador entre o X e O

separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font='arial 40 bold', bg=preto, fg=laranja)
separador.place(x=385, y=15)


# Criando variaveis necessarias para a logica do jogo

jogadorX = "X" 
jogadorO = "O"

pontos_X = 0
pontos_O = 0

tabela = [["", "", ""], ["", "", ""], ["", "", ""]]  # cada lista representa uma linha da tabela e suas posições

jogando = jogadorX

turno = 0
rodadas = 1


# Função pra iniciar o jogo
def iniciarJogo():
    # Função que controla os turnos
    def turnos(valorCaixa, botao, linha, coluna):
        global jogando 
        global turno

        # Variavel para verificar se tem vencedor ou se foi empate
        temVencedor = False

        # Verificando se o jogador cliclou em um botão/caixa vazia 

        if tabela[linha][coluna] != "":
            pass
        else:
            # Verificando quem jogou para atribuir a cor ao simbolo corretamente

            if jogando == jogadorX:
                cor= vermelho
            else:
                cor= azul

            # Marcando jogada na tabela e quem foi o jogador

            botao['fg'] = cor
            botao['text'] = jogando

            # Adicionando valor na tablea passado pelo parametro

            tabela[linha][coluna] = jogando

            # Contando os turnos jogados

            turno += 1

            # Verificando se há algum vencedor

            if turno >= 5:

                # Horizontal
                if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                    temVencedor == True
                    vencedor(jogando)

                elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                    temVencedor == True
                    vencedor(jogando)

                elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                    temVencedor == True
                    vencedor(jogando)

                # Vertical

                elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                    temVencedor == True
                    vencedor(jogando)

                elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                    temVencedor == True
                    vencedor(jogando)

                elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                    temVencedor == True
                    vencedor(jogando)

                # Diagonais

                elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                    temVencedor == True
                    vencedor(jogando)

                elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                    temVencedor == True
                    vencedor(jogando)

                # Verificando se foi empate
                
                elif turno >= 9 and temVencedor == False:
                    vencedor("Foi empate!!")
                    
            # Trocando jogador atual

            if jogando == jogadorX:
                jogando = jogadorO

            else: 
                jogando = jogadorX
            
            # Passando o jogador atual para a Label que exibe quem esta jogando agora
                
            jogandoAgora['text'] = f"É a vez do: '{jogando}'"


    # Função para limpar a tabela apos ter um vencedor
    def vencedor(ganhador):
        global turno
        global contador
        global tabela
        global pontos_X
        global pontos_O
        global labelPontosO
        global labelPontosX
        fimDeJogo = False
        
        # Verificando ganhador para exibir  a mensagem correta

        if ganhador == 'Foi empate!!':
            mensagem = ganhador

            Vencedor = Label(frame_baixo, text=f"{mensagem}", height=1, relief='flat', anchor='center', font='arial 20 bold', bg=preto, fg=laranja)
            Vencedor.place(x=310, y=0)


        else:
            mensagem = f"Jogador '{ganhador}' venceu essa rodada!!"

            Vencedor = Label(frame_baixo, text=f"{mensagem}", height=1, relief='flat', anchor='center', font='arial 20 bold', bg=preto, fg=laranja)
            Vencedor.place(x=180, y=0)


        # Adicionando o ponto ao jogador vencedor

        if ganhador == "X":
            pontos_X += 1
            labelPontosX['text'] = str(pontos_X)

        elif ganhador == "O":
            pontos_O += 1
            labelPontosO['text'] = str(pontos_O)

        # Disabilitando os botões das caixas
        caixa0['state'] = caixa1['state'] = caixa2['state'] = caixa3['state'] = caixa4['state'] = 'disable'
        caixa5['state'] = caixa6['state'] = caixa7['state'] = caixa8['state'] = 'disable'


        # Atribuindo o vencedor para a variavel "VencedorDoJogo"

        if pontos_O > pontos_X:
            VencedorDoJogo = "O"

        elif pontos_X > pontos_O:
            VencedorDoJogo = "X"

        else:
            VencedorDoJogo = "empate"



        if rodadas > 4:
            # Retirando a mensagem de vencedor da rodada 
            Vencedor.destroy()

            # Decretando fim de jogo na variavel
            fimDeJogo = True

            # Chamando a função para finalizar o jogo passando o vencedor como parametro
            finalizarJogo(VencedorDoJogo)


        # Função para ir pro proxima rodada
        def proximaRodada():
            global turno
            global tabela
            global rodadas

            # Mudando para a proxima rodada
            rodadas += 1

            # Reiniciando a tabela para proxima rodada
            tabela = [["", "", ""], ["", "", ""], ["", "", ""]]  # cada lista representa uma linha da tabela e suas posições

            # Reiniciando os turnos para proxima rodada
            turno = 0

            # Passando a rodada atual para a Label
            rodadaAtual['text'] = f"Rodada: {rodadas}"

            # Resetando as caixas/botões para a proxima rodada

            caixa0['text'] = caixa1['text'] = caixa2['text'] = caixa3['text'] = caixa4['text'] = ""
            caixa5['text'] = caixa6['text'] = caixa7['text'] = caixa8['text'] = ""

            # Reativando os botões das caixas
            caixa0['state'] = caixa1['state'] = caixa2['state'] = caixa3['state'] = caixa4['state'] = 'normal'
            caixa5['state'] = caixa6['state'] = caixa7['state'] = caixa8['state'] = 'normal'

            # Destruindo o botão e mensagem de vencedor
            Reiniciar.destroy()
            Vencedor.destroy()


        # utilizando verificação de rodadas e fimDeJogo para que não apareça depois que todas as rodadas acabar
        if rodadas <= 4 and fimDeJogo == False:
            Reiniciar = Button(frame_baixo, command=proximaRodada, text ='Reiniciar', width=10, height=1, font='arial 20 bold',  relief='raised', bg=preto, fg=amarelo)
            Reiniciar.place(x=310, y=470)


    # Função para finalizar o jogo e resetar tudo
    def finalizarJogo(vencedorDoJogo):
        global tabela
        global rodadas
        global pontos_O
        global pontos_X
        global turno


        # Resetando a tabela
        tabela = [["", "", ""], ["", "", ""], ["", "", ""]]  # cada lista representa uma linha da tabela e suas posições

        # Resetando rodadas

        rodadas = 0

        # Resetando os pontos de ambos jogadores

        pontos_X = pontos_O = 0

        # Verificando resultado do ganhador para exibir a mensagem da melhor forma

        if vencedorDoJogo == "empate" :
            # Exibindo a mensagem de empate

            GanhadorDoJogo = Label(frame_baixo, text=f"Empate!!! Que jogo dipustado!", height=1, relief='flat', anchor='center', font='arial 20 bold', bg=preto, fg=laranja)
            GanhadorDoJogo.place(x=195, y=0)

        else:
            # Exibindo o vencedor do jogo

            GanhadorDoJogo = Label(frame_baixo, text=f"O vencedor do jogo foi {vencedorDoJogo}!!!", height=1, relief='flat', anchor='center', font='arial 20 bold', bg=preto, fg=laranja)
            GanhadorDoJogo.place(x=215, y=0)


        # Função que recomeça o jogo
        def recomecarJogo():
            global tabela
            global turno
            global rodadas


            # Reiniciando o jogo destruindo o botão e a mensagem de vencedor
            GanhadorDoJogo.destroy()
            reiniciarJogo.destroy()

            # Resetando tudo para um novo jogo
            turno = 0

            rodadas = 1
            
            tabela = [["", "", ""], ["", "", ""], ["", "", ""]]  # cada lista representa uma linha da tabela e suas posições

            # Resetando os pontos visualmente dos jogadores
            labelPontosX['text'] = labelPontosO['text'] = "0"

            # Chamando o inicarJogo pra voltar tudo do inicio
            iniciarJogo()
        

        # Botão para reiniciar o jogo

        reiniciarJogo = Button(frame_baixo, command=recomecarJogo, text ='Jogar novamente', width=15, height=1, font='arial 20 bold',  relief='raised', bg=preto, fg=amarelo)
        reiniciarJogo.place(x=260, y=470)

    # Label para visualizar em que rodada está

    rodadaAtual = Label(frame_cima, text=f"Rodada: {rodadas}", height=1, relief='flat', anchor='center', font='arial 16 bold', bg=preto, fg=branco)
    rodadaAtual.place(x=345, y=0)


    # Label para visualizar de quem é a vez no turno

    jogandoAgora = Label(frame_cima, text=f"É a vez do: '{jogando}'", height=1, relief='flat', anchor='center', font='arial 16 bold', bg=preto, fg=amarelo)
    jogandoAgora.place(x=325, y=85)


    # Configurando o frame de baixo onde terá os botões para poder jogar

    # linhas verticais

    linhaVertical = Label(frame_baixo, text=' ', height=32, relief='flat', pady=5, anchor='center', bg=branco)
    linhaVertical.place(x=240, y=0)

    linhaVertical = Label(frame_baixo, text=' ', height=32, relief='flat', pady=5, anchor='center', bg=branco)
    linhaVertical.place(x=540, y=0)

    # Linhas horizontais

    linhaHorizontal = Label(frame_baixo, text='',  width=200, height=1, padx=2, relief='flat', anchor='center', bg=branco)
    linhaHorizontal.place(x=20, y=320)

    linhaHorizontal = Label(frame_baixo, text='', width=200, height=1 ,padx=2, relief='flat', anchor='center', bg=branco)
    linhaHorizontal.place(x=20, y=140)

    
    # Configurando os botões para selecionar as posições no jogo

    # botão 0
    caixa0 = Button(frame_baixo, command=lambda:turnos('0', caixa0, 0, 0), text='', width=6,  font='arial 40',  relief='flat', bg=preto,)
    caixa0.place(x=30, y=15)


    # botão 1
    caixa1 = Button(frame_baixo, command=lambda:turnos('1', caixa1, 0, 1), text='', width=8,  font='arial 40',  relief='flat', bg=preto)
    caixa1.place(x=265, y=15)

    # botão 2
    caixa2 = Button(frame_baixo, command=lambda:turnos('2', caixa2, 0, 2), text='', width=6,  font='arial 40',  relief='flat', bg=preto)
    caixa2.place(x=570, y=15)

    # botão 3
    caixa3 = Button(frame_baixo, command=lambda:turnos('3', caixa3, 1, 0), text='', width=6,  font='arial 40',  relief='flat', bg=preto)
    caixa3.place(x=30, y=190)

    # botão 4
    caixa4 = Button(frame_baixo, command=lambda:turnos('4', caixa4, 1, 1), text='', width=8,  font='arial 40',  relief='flat', bg=preto)
    caixa4.place(x=265, y=190)

    # botão 5
    caixa5 = Button(frame_baixo, command=lambda:turnos('5', caixa5, 1, 2), text='', width=6,  font='arial 40',  relief='flat', bg=preto)
    caixa5.place(x=570, y=190)

    # botão 6
    caixa6 = Button(frame_baixo, command=lambda:turnos('6', caixa6, 2, 0), text='', width=6,  font='arial 40',  relief='flat', bg=preto)
    caixa6.place(x=30, y=365)

    # botão 7
    caixa7 = Button(frame_baixo, command=lambda:turnos('7', caixa7, 2, 1), text='', width=8,  font='arial 40',  relief='flat', bg=preto)
    caixa7.place(x=265, y=365)

    # botão 8
    caixa8 = Button(frame_baixo, command=lambda:turnos('8', caixa8, 2, 2), text='', width=6,  font='arial 40',  relief='flat', bg=preto)
    caixa8.place(x=570, y=365)


    # Retirando o botão de inicar jogo
    iniciar.destroy()




# Botao para iniciar o jogo chamando a função iniciarJogo
iniciar = Button(frame_baixo, command=iniciarJogo, text ='Jogar', width=10, height=1, font='arial 20 bold',  relief='raised', bg=preto, fg=amarelo )
iniciar.place(x=305, y=250)


janela.mainloop()