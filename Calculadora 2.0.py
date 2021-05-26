from tkinter import *

calc=Tk()
calc.configure(background="#1C1C1C")
calc.resizable(False, False)#usuario não pode alterar o tamanho da janela
calc.geometry("373x553")

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

i=0
def obter(dato):
	global i
	i+=1
	visor.insert(i, dato)

def click_igual():
	global i

	ecuacion = visor.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			visor.delete(0,END)
			visor.insert(0,result)
			longitud = len(result)
			i = longitud

		except:
			result = 'ERROR'
			visor.delete(0,END)
			visor.insert(0,result)
	else:
		pass

def click_dell():
	#print(i)
	global i 
	if i==-1:
		pass
	else:
		visor.delete(i,last =None)
		i-=1

def deletar():
	visor.delete(0, END)	
	i=0

visor=Entry(calc,bg="#1C1C1C",fg="#F0F8FF",font=("yu 35"),bd=0)
visor.place(x=7,y=70,width=360,height=56)
visor.config(justify='right')#configuração para deixar as string no canto direito

#Filera 0  # outros Blaks..090909...090a0a
bt1=Button(calc,text="CE", bg="#101010",fg="#F0F8FF", pady="20", padx="27",bd=0, command=lambda: deletar(),font=("consolas 15 bold"))
bt1.place(x=5,y=155)
bt1=Button(calc,text="%", bg="#101010",fg="#F0F8FF", pady="20", padx="32",bd=0,font=("consolas 15 bold"))
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
bt1=Button(calc,text="+/-", bg="#010101",fg="#F0F8FF", pady="20", padx="21",bd=0,font=("consolas 15 bold"))
bt1.place(x=5,y=475)
bt1=Button(calc,text="0", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: obter(0),font=("consolas 15 bold"))
bt1.place(x=97,y=475)
bt1=Button(calc,text=".", bg="#010101",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: obter('.'),font=("consolas 15 bold"))
bt1.place(x=188,y=475)
bt1=Button(calc,text="=", bg="#363636",fg="#F0F8FF", pady="20", padx="32",bd=0,command=lambda: click_igual(),font=("consolas 15 bold"))
bt1.place(x=279,y=475)

calc.mainloop()