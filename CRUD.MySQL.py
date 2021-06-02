from mysql.connector import Error #importa a biblioteca de tratamento de erro
import mysql.connector
from tkinter import *

conn = mysql.connector.connect(host='localhost',database='crudtkinter',user='root',password='')# (conn)variavel global para conexão do banco de dados

app=Tk()
app.title("Registro")
app.geometry("1020x720")
app.configure(background="#dde")
app.resizable(False, False)#usuario não pode alterar o tamanho da janela

def mudar(altid,anome,an1,an2):
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    try:
        print(an1)
        print(type(an1))#vendo o tipo primitivo de vn1
        an1=float(an1)#tranformando vn1 para int
        print(type(an1))#confirmando se vn1 é int

        print(an2)
        print(type(an2))#vendo o tipo primitivo de vn2
        an2=float(an2)#tranformando vn2 para int
        print(type(an2))#confirmando se vn2 é int

        media=(an1+an2)/2
        print(media)
        print(type(media))
   
        alterar_dados = "UPDATE aluno SET nome = '{}', nota1 = '{}', nota2 = '{}', media = '{}' WHERE matricula = '{}' ".format(anome,an1,an2,media,altid)

        cursor = conn.cursor()
        cursor.execute(alterar_dados)
        conn.commit()
        print("\n***Registro ALTERADO com sucesso!!!***\n")
        print(cursor.rowcount,"Registros alterado na tabela")#mostra a quantidade de registros na tabela
        msgE1=Label(app, text="Registros alterado com sucesso!\n\nLinhas afetadas:",bg="#dde",fg="green",font="consolas 40",anchor=W).place(x=50,y=250,width=900,height=220)#msg ao cliente
        msgE3=Label(app, text=cursor.rowcount,bg="#dde",fg="green",font="consolas 40",anchor=W).place(x=750,y=390,width=300,height=60)# msg ao cliente 
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=450,y=470,width=130,height=50)# Cria o botão e envia para função Gravar dados
        
    except ValueError as erro:
        msgE2=Label(app, text="Falha ao atualizar os dados",bg="#dde",fg="red",font="consolas 30",anchor=W).place(x=50,y=250,width=900,height=60)# msg ao cliente
        msgE3=Label(app, text=erro,bg="#dde",fg="red",font="consolas 20",anchor=W).place(x=50,y=300,width=900,height=60)# msg ao cliente
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=400,y=500,width=130,height=50)# Cria o botão e envia para função Gravar dados
        print(erro)
        MENU=(input("Pressione qualquer tecla para voltar ao menu...."))
        
        
    
def GravaDados(vnome,vmatri,vn1,vn2):#função para gravar dados
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")#fundo padrão para sobrepor funções anteriores
    fr_quadro2.place(x=0,y=0,width=1020,height=720)

    try:#Tratamento de erro
        print(vn1)
        print(type(vn1))#vendo o tipo primitivo de vn1
        vn1=float(vn1)#tranformando vn1 para int
        print(type(vn1))#confirmando se vn1 é int

        print(vn2)
        print(type(vn2))#vendo o tipo primitivo de vn2
        vn2=float(vn2)#tranformando vn2 para int
        print(type(vn2))#confirmando se vn2 é int

        media=(vn1+vn2)/2
        print(media)
        print(type(media))

        sql ="INSERT INTO aluno (matricula,nome,nota1,nota2,media) VALUES('{}','{}','{}','{}','{}')".format(vmatri,vnome,vn1,vn2,media)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()#Salvando alterações 
    except ValueError as erro:# tratamento de erro caso nenhum valor nos campos
        msgE2=Label(app, text="Falha ao salvar os dados",bg="#dde",fg="red",font="consolas 30",anchor=W).place(x=50,y=250,width=900,height=60)# msg ao cliente
        msgE3=Label(app, text=erro,bg="#dde",fg="red",font="consolas 20",anchor=W).place(x=50,y=300,width=900,height=60)# msg ao cliente
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=450,y=400,width=130,height=50)#Voltar
    except mysql.connector.errors.IntegrityError as erro:#ratamento de erro caso chave primaria iguais
        msgE2=Label(app, text="Falha ao salvar os dados",bg="#dde",fg="red",font="consolas 30",anchor=W).place(x=50,y=250,width=900,height=60)# msg ao cliente
        msgE3=Label(app, text=erro,bg="#dde",fg="red",font="consolas 20",anchor=W).place(x=50,y=300,width=900,height=60)# msg ao cliente
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=450,y=400,width=130,height=50)#Voltar
    else:
        msgE1=Label(app, text="Arquivo Cadastrado com sucesso!",bg="#dde",fg="green",font="consolas 40",anchor=W).place(x=50,y=250,width=900,height=60)#msg ao cliente
        print("\n***Registro INSERIDO com sucesso!!!***\n")
        print(cursor.rowcount,"Registros na tabela")#mostra a quantidade de registros na tabela
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=450,y=400,width=130,height=50)#Vol
        

def registrar():
    
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)

    altid=Label(app, text="CADASTRAR DADOS",bg="#dde",fg="black",font="consolas 35 bold",anchor=W).place(x=300,y=20,width=600,height=40)

    vnome=Label(app, text="Nome:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=80,width=600,height=40)#Nome
    vnome=Entry(app, textvariable=vnome,font="times 20")
    vnome.place(x=300,y=120,width=400,height=40)

    vmatri=Label(app, text="Matricula:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=190,width=600,height=40)#Matricula
    vmatri=Entry(app, textvariable=vmatri,font="times 20")
    vmatri.place(x=300,y=230,width=400,height=40)

    vn1=Label(app, text="Nota 1:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=300,width=600,height=40)#Nota 1
    vn1=Entry(app, textvariable=vn1,font="times 20")
    vn1.place(x=300,y=340,width=400,height=40)

    vn2=Label(app, text="Nota 2:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=400,width=600,height=40)#Nota 2
    vn2=Entry(app, textvariable=vn2,font="times 20")
    vn2.place(x=300,y=440,width=400,height=40)
        
    Envia = Button(app, text="Enviar",bg="#808080",fg="#010101", command=lambda:GravaDados(vnome.get(),vmatri.get(),vn1.get(),vn2.get()),font="consolas 25 bold").place(x=390,y=500,width=200,height=50)# Cria o botão e envia para função Gravar dados
    


def consultar():
    conn = mysql.connector.connect(host='localhost',database='crudtkinter',user='root',password='')# (conn)variavel global para conexão do banco de dados
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    registros=Label(app, text="REGISTROS",bg="#dde",fg="black",font="consolas 60 bold",).place(x=220,y=15,width=600,height=80)
    
    try:
        query = "SELECT * FROM aluno" 
        cursor = conn.cursor()#apontador
        cursor.execute(query)#O cursor aponta para todas as respostar das execuções da query
        linhas = cursor.fetchall()#(fetchall)recebe todas as resposta da base de dados
        print("Numero total de registros retornados: ",cursor.rowcount)#conta os registros da consulta
        print("\n***Pessoas Cadastradas***\n")

        Label(app,text="txt",bg="#dde")
        txt=Text(app)
        txt.config(font="consolas 15 bold")
        txt.place(x=10,y=100,width="1000",height="600")

        colunas = 0
        for colunas in linhas: #cria uma estrutura de repatição que é apontada atraves dos vetores
                 cp1 ='Matricula:',colunas[0],'Nome:',colunas[1],'nota1:',colunas[2],'nota2:',colunas[3],'media:',colunas[4]
                 txt.insert(0.0,cp1)
                 separa="\n------------------------------------------------------------------------------------------"
                 txt.insert(0.0,separa)
        if linhas == linhas:
                 voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=10,y=20,width=130,height=50)#Voltar
                   
    except Error as erro:#Tratamento de erro
         print("Erro ao acessar o SGBD",erro)
    finally:#fechando conexão
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("***Conexão Encerrada***") 
            MENU=(input("Pressione qualquer tecla para voltar ao menu...."))
           

def alterar():
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    altid=Label(app, text="ATUALIZAR DADOS",bg="#dde",fg="black",font="consolas 35 bold",anchor=W).place(x=300,y=20,width=600,height=40)
    conn = mysql.connector.connect(host='localhost',database='crudtkinter',user='root',password='')# (conn)variavel global para conexão do banco de dados


    altid=Label(app, text="Matricula a ser Alterada:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=80,width=600,height=40)#Matricula
    altid=Entry(app, textvariable=altid,font="times 20")
    altid.place(x=300,y=120,width=400,height=40)

    anome=Label(app, text="Nome a ser Alterado:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=190,width=600,height=40)#Nome
    anome=Entry(app, textvariable=anome,font="times 20")
    anome.place(x=300,y=230,width=400,height=40)

    an1=Label(app, text="Nota 1 a ser Alterada:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=300,width=600,height=40)#Nota 1
    an1=Entry(app, textvariable=an1,font="times 20")
    an1.place(x=300,y=340,width=400,height=40)

    an2=Label(app, text="Nota 2 a ser Alterada:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=400,width=600,height=40)#Nota 2
    an2=Entry(app, textvariable=an2,font="times 20")
    an2.place(x=300,y=440,width=400,height=40)

    Envia = Button(app, text="Enviar",bg="#808080",fg="#010101", command=lambda:mudar(altid.get(),anome.get(),an1.get(),an2.get()),font="consolas 25 bold").place(x=380,y=500,width=200,height=50)# Cria o botão e envia para função Gravar dados


def delldados(pesqId):
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    try:
        dell_dados = "DELETE FROM aluno WHERE aluno.matricula = {}".format(pesqId)
        cursor = conn.cursor()
        cursor.execute(dell_dados)
        conn.commit()
        print("\n***Registro EXCLUIDO com sucesso!!!***\n")
        print(cursor.rowcount,"Registros alterado na tabela")#mostra a quantidade de registros na tabela
        msgE1=Label(app, text="Registro EXCLUIDO com sucesso!\n\nLinhas afetadas:",bg="#dde",fg="green",font="consolas 40",anchor=W).place(x=50,y=250,width=900,height=220)#msg ao cliente
        msgE3=Label(app, text=cursor.rowcount,bg="#dde",fg="green",font="consolas 40",anchor=W).place(x=750,y=390,width=300,height=60)# msg ao cliente 
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=450,y=470,width=130,height=50)# Cria o botão e envia para função Gravar dados
        
    except Error as erro:
        print("ok")
        msgE2=Label(app, text="Falha ao excluir os dados",bg="#dde",fg="red",font="consolas 30",anchor=W).place(x=50,y=250,width=900,height=60)# msg ao cliente
        msgE3=Label(app, text=erro,bg="#dde",fg="red",font="consolas 18",anchor=W).place(x=50,y=300,width=900,height=60)# msg ao cliente
        voltar = Button(app, text="voltar",bg="#808080",fg="#010101",font="consolas 25 bold",command=lambda: menu()).place(x=450,y=400,width=130,height=50)# Cria o botão e envia para função Gravar dados
        

def excluir():
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    
    pesqId=Label(app, text="Matricula a ser Excluida:",bg="#dde",fg="black",font="consolas 15",anchor=W).place(x=300,y=180,width=600,height=40)#Matricula
    pesqId=Entry(app, textvariable=pesqId,font="times 20")
    pesqId.place(x=300,y=220,width=400,height=40)

    Envia = Button(app, text="Enviar",bg="#808080",fg="#010101", command=lambda:delldados(pesqId.get()),font="consolas 25 bold").place(x=380,y=400,width=200,height=50)# Cria o botão e envia para função Gravar dados
    

        


fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
fr_quadro2.place(x=0,y=0,width=1020,height=720)
menu=Label(app, text="MENU",bg="#dde",fg="black",font="consolas 60 bold",).place(x=220,y=50,width=600,height=80)
bt1=Button(app,text="Registrar", bg="#808080",fg="#010101", pady="40", padx="50",bd=10,font=("consolas 40 bold"),command=lambda: registrar())
bt1.place(x=70,y=180)

bt2=Button(app,text="Consultar", bg="#808080",fg="#010101", pady="40", padx="36",bd=10,font=("consolas 40 bold"),command=lambda: consultar())
bt2.place(x=550,y=180)

bt3=Button(app,text="Atualizar", bg="#808080",fg="#010101", pady="40", padx="50",bd=10,font=("consolas 40 bold"),command=lambda: alterar())
bt3.place(x=70,y=450)

bt4=Button(app,text="Excluir", bg="#808080",fg="#010101", pady="40", padx="64",bd=10,font=("consolas 40 bold"),command=lambda: excluir())
bt4.place(x=550,y=450)
''''
barrademenu=Menu(app)
vmenu=Menu(barrademenu)
vmenu.add_command(label="MENU",command=lambda: menu())
vmenu.config(font=("system 40 bold"))
'''
def menu():
    fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#dde")
    fr_quadro2.place(x=0,y=0,width=1020,height=720)
    menu=Label(app, text="MENU",bg="#dde",fg="black",font="consolas 60 bold",).place(x=220,y=50,width=600,height=80)
    bt1=Button(app,text="Registrar", bg="#808080",fg="#010101", pady="40", padx="50",bd=10,font=("consolas 40 bold"),command=lambda: registrar())
    bt1.place(x=70,y=180)

    bt2=Button(app,text="Consultar", bg="#808080",fg="#010101", pady="40", padx="36",bd=10,font=("consolas 40 bold"),command=lambda: consultar())
    bt2.place(x=550,y=180)

    bt3=Button(app,text="Atualizar", bg="#808080",fg="#010101", pady="40", padx="50",bd=10,font=("consolas 40 bold"),command=lambda: alterar())
    bt3.place(x=70,y=450)

    bt4=Button(app,text="Excluir", bg="#808080",fg="#010101", pady="40", padx="64",bd=10,font=("consolas 40 bold"),command=lambda: excluir())
    bt4.place(x=550,y=450)
'''
vmenu.add_separator()
vmenu.add_command(label="Fechar",command=quit)
barrademenu.add_cascade(label="Contatos",menu=vmenu)
app.config(menu=vmenu)
'''
app.mainloop()


