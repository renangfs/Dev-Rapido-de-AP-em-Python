from tkinter import *
#https://www.youtube.com/watch?v=pxi8ec-mqAQ&t=26s
calc=Tk()
calc.title("Jogo da Velha")
calc.configure(background="#1C1C1C")
calc.resizable(False, False)#usuario não pode alterar o tamanho da janela
calc.geometry("700x640")
calc.attributes("-alpha",1)#configuração para deixar a calculadora trasparente

#0=PRIMEIRO 1=X 2=O

#Filera 1
XO = 0
def cb1():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=30)
        XO = 2
        print(XO)
        print("if cb1 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=30)
        XO = 2
        print("if cb1 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=30)
        XO = 1
        print("if cb1 3")
def cb2():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=30)
        XO = 2
        print(XO)
        print("if cb2 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=30)
        XO = 2
        print("if cb2 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=30)
        XO = 1
        print("if cb2 3")
def cb3():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=30)
        XO = 2
        print(XO)
        print("if cb3 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=30)
        XO = 2
        print("if cb3 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=30)
        XO = 1
        print("if cb3  3")
#filera 2
def cb4():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=230)
        XO = 2
        print(XO)
        print("if cb4 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=230)
        XO = 2
        print("if cb4 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=230)
        XO = 1
        print("if cb4 3")
def cb5():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=230)
        XO = 2
        print(XO)
        print("if cb5 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=230)
        XO = 2
        print("if cb5 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=230)
        XO = 1
        print(XO)
        print("if cb5 3")
def cb6():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=230)
        XO = 2
        print(XO)
        print("if cb6 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=230)
        XO = 2
        print("if cb6 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=230)
        XO = 1
        print("if cb6 3")
#filera 3
def cb7():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=430)
        XO = 2
        print(XO)
        print("if cb4 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=430)
        XO = 2
        print("if cb4 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=10,y=430)
        XO = 1
        print("if cb4 3")
def cb8():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=430)
        XO = 2
        print(XO)
        print("if cb5 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=430)
        XO = 2
        print("if cb5 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=240,y=430)
        XO = 1
        print(XO)
        print("if cb5 3")
def cb9():
    global XO
    if XO == 0:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=430)
        XO = 2
        print(XO)
        print("if cb6 1")
    elif XO == 1:
        bt1=Button(calc,text="X", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=430)
        XO = 2
        print("if cb6 2")
    elif XO == 2:
        bt1=Button(calc,text="O", bg="#808080",fg="#010101", pady="80", padx="100",bd=0,font=("consolas 15 bold"))
        bt1.place(x=470,y=430)
        XO = 1
        print("if cb6 3")
#Filera 1 
bt1=Button(calc,bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb1())
bt1.place(x=10,y=30)
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb2())
bt1.place(x=240,y=30)
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb3())
bt1.place(x=470,y=30)

#Filera 2
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb4())
bt1.place(x=10,y=230)
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb5())
bt1.place(x=240,y=230)
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb6())
bt1.place(x=470,y=230)

#Filera 3
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb7())
bt1.place(x=10,y=430)
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb8())
bt1.place(x=240,y=430)
bt1=Button(calc, bg="#808080",fg="#010101", pady="80", padx="105",bd=0,font=("consolas 15 bold"),command=lambda: cb9())
bt1.place(x=470,y=430)

calc.mainloop()