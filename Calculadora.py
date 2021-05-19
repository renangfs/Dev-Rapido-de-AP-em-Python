from tkinter import *

calc=Tk()
calc.title("Calculadora")
calc.configure(background="#1C1C1C")
calc.attributes("-alpha",0.9)



def click_soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def click_sub():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "subtracao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def click_divi():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "divisao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)    

def click_mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "multiplicacao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)    

def click_igual():
    segundo_numero= visor.get()
    visor.delete(0,END) 
    if matematica == "soma":
        visor.insert(0,p_numero+float(segundo_numero))
    if matematica == "subtracao":
        visor.insert(0,p_numero-float(segundo_numero))
    if matematica == "multiplicacao":
        visor.insert(0,p_numero*float(segundo_numero))
    if matematica == "divisao":
        visor.insert(0,p_numero/float(segundo_numero))

def click_ponto():
    visor.insert(END,".")

def deletar():
    visor.delete(0,END)

def click_button(numero):#função para pegar os numeros
    atual = visor.get()
    visor.delete(0,END)
    visor.insert(END, str(atual)+ str(numero))


lb1=Label(calc,text="Calculadora",bg="#1C1C1C",fg="#F0F8FF", font=("consolas 25 bold"))
lb1.pack()
visor=Entry(calc,bg="#1C1C1C",fg="#F0F8FF",font=("yu 25 "),bd=0)
visor.place(x=7,y=70,width=360,height=60)

#Filera 0  # outros Blaks..090909...090a0a
bt1=Button(calc,text="CE", bg="#101010",fg="#F0F8FF", pady="20", padx="27",bd=0, command=deletar,font=("consolas 15 bold"))
bt1.place(x=5,y=155)
bt1=Button(calc,text="X", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=click_mult,font=("consolas 15 bold"))
bt1.place(x=97,y=155)
bt1=Button(calc,text="/", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=click_divi,font=("consolas 15 bold"))
bt1.place(x=188,y=155)
bt1=Button(calc,text="<=", bg="#101010",fg="#F0F8FF", pady="20", padx="28",bd=0,font=("consolas 15 bold"))
bt1.place(x=279,y=155)
#Filera 1
bt1=Button(calc,text="7", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(7),font=("consolas 15 bold"))
bt1.place(x=5,y=235)
bt1=Button(calc,text="8", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(8),font=("consolas 15 bold"))
bt1.place(x=97,y=235)
bt1=Button(calc,text="9", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(9),font=("consolas 15 bold"))
bt1.place(x=188,y=235)
bt1=Button(calc,text="+", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=click_soma,font=("consolas 15 bold"))
bt1.place(x=279,y=235)
#Filera 2
bt1=Button(calc,text="4", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(4),font=("consolas 15 bold"))
bt1.place(x=5,y=315)
bt1=Button(calc,text="5", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(5),font=("consolas 15 bold"))
bt1.place(x=97,y=315)
bt1=Button(calc,text="6", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(6),font=("consolas 15 bold"))
bt1.place(x=188,y=315)
bt1=Button(calc,text="-", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=click_sub,font=("consolas 15 bold"))
bt1.place(x=279,y=315)
#Filera 3 #85
bt1=Button(calc,text="1", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(1),font=("consolas 15 bold"))
bt1.place(x=5,y=395)
bt1=Button(calc,text="2", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(2),font=("consolas 15 bold"))
bt1.place(x=97,y=395)
bt1=Button(calc,text="3", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:click_button(3),font=("consolas 15 bold"))
bt1.place(x=188,y=395)
bt1=Button(calc,text="+", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=click_soma,font=("consolas 15 bold"))
bt1.place(x=279,y=395)
#Filera 4 #85
bt1=Button(calc,text="+/-", bg="#101010",fg="#F0F8FF", pady="20", padx="21",bd=0,font=("consolas 15 bold"))
bt1.place(x=5,y=475)
bt1=Button(calc,text="0", bg="#000000",fg="#F0F8FF", pady="20", padx="32",bd=0,command= lambda:click_button(0),font=("consolas 15 bold"))
bt1.place(x=97,y=475)
bt1=Button(calc,text=".", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0,command=click_ponto,font=("consolas 15 bold"))
bt1.place(x=188,y=475)
bt1=Button(calc,text="=", bg="#1C1C1C",fg="#F0F8FF", pady="20", padx="32",bd=0,command=click_igual,font=("consolas 15 bold"))
bt1.place(x=279,y=475)



calc.resizable(False, False)#usuario não pode alterar o tamanho da janela
calc.geometry("373x553")
calc.mainloop()
