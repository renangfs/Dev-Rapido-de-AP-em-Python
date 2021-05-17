from tkinter import *
import os


def GravaDados(vnome,vmatri,vn1,vn2):#função para mostrar nome no terminal e ao lado do campo de registro 
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    #media=vn1+vn2/2 problemas ao calcular media
    try:#Tratamento de erro
        arquivo= open ("C:\\Users\\renan\\Desktop\\pasta\\teste.txt", "a")
        arquivo.write("Nome:"+vnome+"      Matricula:"+vmatri+"\n")
        arquivo.write("Nota 1: "+vn1+"      Nota 2: "+vn2+"     Media: #media""\n\n")
        arquivo.close()
        msgE1=Label(app, text="Dados cadastrados com sucesso!",bg="#dde",fg="green",font="consolas 15",anchor=W).place(x=370,y=260,width=400,height=20)#Esolha da operação
    except IOError as erro:    
        msgE2=Label(app, text="Falha ao salvar os dados",bg="#dde",fg="red",font="consolas 15",anchor=W).place(x=410,y=260,width=300,height=20)#Esolha da operação
        msgE3=Label(app, text=erro,bg="#dde",fg="red",font="consolas 15",anchor=W).place(x=100,y=280,width=900,height=20)#Esolha da operação


def Criar():#função para mostrar nome no terminal e ao lado do campo de registro 
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)

    label = Label(app,
    text="Criar",
    bg="#dde",
    fg="blue",
    font="system 20 bold")
    label.place(x=10,y=10,width=1000,height=20)


    try:#Tratamento de erro
        arquivo= open ("C:\\Users\\renan\\Desktop\\pasta\\teste.txt", "x")# "X" apenas cria o arquivo 
        print("\n\n****Arquivo Criado com sucesso!****\n\n")
        msgE1=Label(app, text="Arquivo Criado com sucesso!",bg="#dde",fg="green",font="consolas 15",anchor=W).place(x=370,y=260,width=300,height=20)#Esolha da operação
        arquivo.close()
    except IOError as erro:#Tratamento de erro 
        print("-----------------------------------")
        print("Arquivo já existente !!!")
        print("Descrição: ",erro)
        print("Término do programa")
        msgE2=Label(app, text="arquivo já  existente",bg="#dde",fg="red",font="consolas 15",anchor=W).place(x=410,y=260,width=300,height=20)#Esolha da operação
        msgE3=Label(app, text=erro,bg="#dde",fg="red",font="consolas 15",anchor=W).place(x=100,y=280,width=900,height=20)#Esolha da operação
        print("-----------------------------------")
        MENU=(input("Pressione qualquer tecla para voltar ao menu....")) 

def Ler(): 
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")

    fr_quadro2.place(x=0,y=0,width=1020,height=720)

    label = Label(app,
    text="Lista de Cadastros",
    bg="#dde",
    fg="blue",
    font="system 20 bold")
    label.place(x=10,y=10,width=1000,height=20)
 

    t=Text(app,font="consolas 15")
    t.place(x=10,y=35,width=1000,height=650)
    try:
        arquivo = open("C:\\Users\\renan\\Desktop\\pasta\\teste.txt", "r")
        #print (arquivo.read()) #para saida grafica
        copia = arquivo.read()
        t.insert(0.0,copia)
        arquivo.close()
    except FileNotFoundError as erro:
        msgE2=Label(app, text="arquivo não encontrado",bg="white",fg="red",font="consolas 15",anchor=W).place(x=410,y=260,width=300,height=20)#Esolha da operação
        msgE2=Label(app, text=erro,bg="white",fg="red",font="consolas 15",anchor=W).place(x=30,y=280,width=950,height=20)#Esolha da operação
   


def Acrescentar():
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)

    label = Label(app,
    text="Cadastrar",
    bg="#dde",
    fg="blue",
    font="system 20 bold")
    label.place(x=10,y=10,width=1000,height=20)

    vnome=Label(app, text="Nome:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=40,width=600,height=40)#Esolha da operação
    vnome=Entry(app, textvariable=vnome,font="times 20")
    vnome.place(x=300,y=80,width=400,height=40)

    vmatri=Label(app, text="Matricula:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=150,width=600,height=40)#Esolha da operação
    vmatri=Entry(app, textvariable=vmatri,font="times 20")
    vmatri.place(x=300,y=190,width=400,height=40)

    vn1=Label(app, text="Nota 1:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=250,width=600,height=40)#Esolha da operação
    vn1=Entry(app, textvariable=vn1,font="times 20")
    vn1.place(x=300,y=290,width=400,height=40)

    vn2=Label(app, text="Nota 2:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=350,width=600,height=40)#Esolha da operação
    vn2=Entry(app, textvariable=vn2,font="times 20")
    vn2.place(x=300,y=390,width=400,height=40)



    Envia = Button(app, text="Enviar", command=lambda:GravaDados(vnome.get(),vmatri.get(),vn1.get(),vn2.get()),font="consolas 25",anchor=W).place(x=430,y=500,width=130,height=50)# Cria o botão e envia para função mostrar nome
    Envia.pack()       



def Excluir():
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    try:
        os.path.exists("C:\\Users\\renan\\Desktop\\pasta\\teste.txt")
        os.remove("C:\\Users\\renan\\Desktop\\pasta\\teste.txt")
        msgE1=Label(app, text="Arquivo Removido!",bg="#dde",fg="green",font="consolas 15",anchor=W).place(x=400,y=260,width=400,height=20)#Esolha da 
    except IOError as erro:#Tratamento de erro 
        msgE1=Label(app, text="Arquivo Inesistente para ser excluido",bg="#dde",fg="red",font="consolas 15",anchor=W).place(x=310,y=260,width=500,height=20)#Esolha da operação
        msgE1=Label(app, text=erro,bg="#dde",fg="red",font="consolas 15",anchor=W).place(x=15,y=280,width=950,height=20)#Esolha da operação



app=Tk()
app.title("TITULO")
app.geometry("1020x720")
app.configure(background="#dde")

barrademenu=Menu(app)
vmenu=Menu(barrademenu)
vmenu.add_command(label="Criar",command=Criar)

vmenu.add_command(label="Ler",command=Ler)

vmenu.add_command(label="Acrescentar",command=Acrescentar)

vmenu.add_command(label="Excluir",command=Excluir)

vmenu.add_separator()
vmenu.add_command(label="Fechar",command=quit)
barrademenu.add_cascade(label="Contatos",menu=vmenu)
app.config(menu=vmenu)

app.mainloop()