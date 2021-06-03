from tkinter import *
from tkinter.messagebox import showinfo

velha=Tk()
velha.title("Jogo da Velha")
velha.configure(background="#1C1C1C")
velha.resizable(False, False)#usuario não pode alterar o tamanho da janela
velha.geometry("700x640")
velha.attributes("-alpha",1)#configuração para deixar a calculadora trasparente
QTD = 0
XO = 1
MATRIZ=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def cb1(l,c,posx,posy):#Linha e coluna que vão ser acionadas quando ocorrer o click no botão
    global QTD
    global XO
    global MATRIZ
    QTD += 1
    MATRIZ[l][c]=XO# 1= X.....2= O
    print("cliks",QTD)
    print(MATRIZ)
    print("Mostra matriz:",MATRIZ[0][0],MATRIZ[0][1],MATRIZ[0][2])
    print("Mostra matriz:",MATRIZ[1][0],MATRIZ[1][1],MATRIZ[1][2])
    print("Mostra matriz:",MATRIZ[2][0],MATRIZ[2][1],MATRIZ[2][2])

    symbol = "X"
    if(XO == 2):
        symbol = "O"

    bt1=Button(velha,text=symbol, bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
    bt1.place(x=posx,y=posy)
    if QTD >=9:
        showinfo(title="Velha",
                 message="Empate......Fim de jogo")
    else:
        if QTD >=5: # Quantidade de cliks minimos para iniciar a verificação
            if(MATRIZ[0][0] == MATRIZ[0][1] and MATRIZ[0][0] == MATRIZ[0][2] and MATRIZ[0][0] != 0):# OK
                print("Vitoria primeira linha.............................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
                
            elif(MATRIZ[1][0] == MATRIZ[1][1] and MATRIZ[1][0] == MATRIZ[1][2] and MATRIZ[1][0] != 0):# OK
                print("Vitoria segunda linha...............................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
            elif(MATRIZ[2][0] == MATRIZ[2][1] and MATRIZ[2][0] == MATRIZ[2][2] and MATRIZ[2][0] != 0):# OK
                print("Vitoria terceira linha..................................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
            elif(MATRIZ[0][0] == MATRIZ[1][0] and MATRIZ[0][0] == MATRIZ[2][0] and MATRIZ[0][0] != 0):# OK
                print("Vitoria primeira coluna.................................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
            elif(MATRIZ[0][1] == MATRIZ[1][1] and MATRIZ[0][1] == MATRIZ[2][1] and MATRIZ[0][1] != 0):# OK
                print("Vitoria segunda coluna.................................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
            elif(MATRIZ[0][2] == MATRIZ[1][2] and MATRIZ[0][2] == MATRIZ[2][2] and MATRIZ[0][2] != 0):# OK
                print("Vitoria terceira coluna...........................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
            elif(MATRIZ[0][0] == MATRIZ[1][1] and MATRIZ[0][0] == MATRIZ[2][2] and MATRIZ[0][0] != 0):# OK
                print("Vitoria diagonal principal...........................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
            elif(MATRIZ[2][0] == MATRIZ[1][1] and MATRIZ[2][0] == MATRIZ[0][2] and MATRIZ[2][0] != 0):# OK
                print("Vitoria segunda diagonal....................")
                if XO == 1:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'X' GANHOU")
                else:
                    showinfo(title="GANHADOR",
                    message="O jogador que estava jogando com o 'O' GANHOU")
    if(XO == 1):
        XO = 2
    else:
        XO = 1
#Filera 1 
bt1=Button(velha,bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(0,0,10,30))
bt1.place(x=10,y=30)
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(0,1,240,30))
bt1.place(x=240,y=30)
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(0,2,470,30))
bt1.place(x=470,y=30)
#Filera 2
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(1,0,10,230))
bt1.place(x=10,y=230)
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(1,1,240,230))
bt1.place(x=240,y=230)
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(1,2,470,230))
bt1.place(x=470,y=230)
#Filera 3
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(2,0,10,430))
bt1.place(x=10,y=430)
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(2,1,240,430))
bt1.place(x=240,y=430)
bt1=Button(velha, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1(2,2,470,430))
bt1.place(x=470,y=430)

velha.mainloop()
