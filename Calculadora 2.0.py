from tkinter import *
#https://www.youtube.com/watch?v=pxi8ec-mqAQ&t=26s
calc=Tk()
calc.title("Calculadora")
calc.configure(background="#1C1C1C")
calc.resizable(False, False)#usuario não pode alterar o tamanho da janela
calc.geometry("373x553")
calc.attributes("-alpha",1)#configuração para deixar a calculadora trasparente

i=0
def obter(dato):
	global i
	i+=1
	visor.insert(i, dato)
def click_igual():
	global i
	equacao = visor.get()
	if i !=0:		
		try:
			result = str(eval(equacao))#calcula a equação
			visor.delete(0,END)#apaga o visor
			visor.insert(0,result)#insere o resultado
			longitud = len(result)#pega o comprimento de numeros do resultado
			i = longitud# i recebe o comprimento do resultado
		except:#tratamento de erro caso de erro na equação
			result = 'ERROR'
			visor.delete(0,END)
			visor.insert(0,result)
	else:
		pass
def click_dell():
	global i 
	if i==-1:
		pass
	else:
		visor.delete(i,last =None)#deleta o ultimo termo do comprimento do resultado
		i-=1
def deletar():
	visor.delete(0, END)	
	i=0

def inverte():
	inv = visor.get()
	invert = float(inv)
	if invert>0:
		inverte = invert-(invert*2)#transforma em negativo
		print(inverte)
		inve = str(inverte)
		visor.delete(0,END)
		visor.insert(0,inve)
	elif invert<0:
		inverte = abs(invert)#transforma em positivo
		print(inverte)
		inve = str(inverte)
		visor.delete(0,END)
		visor.insert(0,inve)

visor=Entry(calc,bg="#1C1C1C",fg="#F0F8FF",font=("yu 35"),bd=0)
visor.place(x=7,y=70,width=360,height=56)
visor.config(justify='right')#configuração para deixar as string no canto direito

#Filera 0  # outros Blaks..090909...090a0a
bt1=Button(calc,text="CE", bg="#101010",fg="#F0F8FF", pady="20", padx="27",bd=0, command=lambda: deletar(),font=("consolas 15 bold"))
bt1.place(x=5,y=155)
bt1=Button(calc,text="%", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: obter('%'),font=("consolas 15 bold"))
bt1.place(x=97,y=155)
bt1=Button(calc,text="/", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter('/'),font=("consolas 15 bold"))
bt1.place(x=188,y=155)
bt1=Button(calc,text="⌫", bg="#101010",fg="#F0F8FF", pady="20", padx="25",bd=0,font=("consolas 15 "),command=lambda: click_dell())
bt1.place(x=279,y=155)

#Filera 1 
bt1=Button(calc,text="7", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(7),font=("consolas 15 bold"))
bt1.place(x=5,y=235)
bt1=Button(calc,text="8", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda: obter(8),font=("consolas 15 bold"))
bt1.place(x=97,y=235)
bt1=Button(calc,text="9", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command= lambda:obter(9),font=("consolas 15 bold"))
bt1.place(x=188,y=235)
bt1=Button(calc,text="X", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter('*'),font=("consolas 15 bold"))
bt1.place(x=279,y=235)

#Filera 2
bt1=Button(calc,text="4", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(4),font=("consolas 15 bold"))
bt1.place(x=5,y=315)
bt1=Button(calc,text="5", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(5),font=("consolas 15 bold"))
bt1.place(x=97,y=315)
bt1=Button(calc,text="6", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(6),font=("consolas 15 bold"))
bt1.place(x=188,y=315)
bt1=Button(calc,text="-", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter('-'),font=("consolas 15 bold"))
bt1.place(x=279,y=315)


#Filera 3
bt1=Button(calc,text="1", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(1),font=("consolas 15 bold"))
bt1.place(x=5,y=395)
bt1=Button(calc,text="2", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(2),font=("consolas 15 bold"))
bt1.place(x=97,y=395)
bt1=Button(calc,text="3", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter(3),font=("consolas 15 bold"))
bt1.place(x=188,y=395)
bt1=Button(calc,text="+", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0, command=lambda: obter('+'),font=("consolas 15 bold"))
bt1.place(x=279,y=395)

#Filera 04
bt1=Button(calc,text="+/-", bg="#010101",fg="#F0F8FF", pady="20", padx="21",bd=0,command=lambda: inverte(),font=("consolas 15 bold"))
bt1.place(x=5,y=475)
bt1=Button(calc,text="0", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: obter(0),font=("consolas 15 bold"))
bt1.place(x=97,y=475)
bt1=Button(calc,text=".", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: obter('.'),font=("consolas 15 bold"))
bt1.place(x=188,y=475)
bt1=Button(calc,text="=", bg="#363636",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: click_igual(),font=("consolas 15 bold"))
bt1.place(x=279,y=475)

calc.mainloop()
