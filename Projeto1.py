import tkinter #importa a biblioteca Tkinder
from tkinter import * #importando tudo da biblioteca

def mostrarNome(nome):#função para mostrar nome no terminal e ao lado do campo de registro 
    print("My name is " + nome)
    label = Label(window, text = nome)
    label.pack(side=LEFT)   

window = tkinter.Tk() #criando uma intancia da classe Tkinter
window.title("Titulo Python") #Definindo titulo
window.minsize("300","100") #Definindo tamanho

label = Label(window, text="Qual seu nome?")# Cria uma label nome
label.pack(side=LEFT)

labelInput = StringVar()#cria uma box para gravar caracteres
labelInput = Entry(window, textvariable=labelInput)
labelInput.pack(side=LEFT)

button = Button(window, text="Botão", command=lambda: mostrarNome(labelInput.get()))# Cria o botão e
button.pack(side=RIGHT)# enviapara função mostrar nome

window.mainloop() #criando loop para fazer a janela executar


