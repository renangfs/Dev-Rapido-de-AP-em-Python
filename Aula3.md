### 23/03/2021
Link: http://portaldoaluno.webaula.com.br/Classroom/index.html?id=3700126&classId=911751&topicId=0&p0=03c7c0ace395d80182db07ae2c30f034&enableForum=S&enableMessage=N&enableClassMate=N
<h1 align="center">Manipulação de dados com PYTHON<h1>
 
### Criação de arquivo texto:

arquivo = open("arquivo1.txt","w")<br>
arquivo.write("Primeira linha do meu arquivo texto\n")<br>
arquivo.write("Segunda linha do meu arquivo texto\n")<br>
arquivo.write("Terceira linha do meu arquivo texto")<br>
arquivo.close()<br>

### Leitura de arquivo texto:

arquivo = open("arquivo1.txt","r")<br>
print (arquivo.read())<br>
arquivo.close()<br>

### Acrescentar dados no arquivo texto:

Modo1:<br>
arquivo = open("arquivo1.txt","a")<br>
arquivo.write("\nQuarta linha do meu arquivo texto\n")<br><br>
arquivo.write("Quinta linha do meu arquivo texto\n")<br>
arquivo.write("Sexta linha do meu arquivo texto")<br>
arquivo.close()<br>

Modo2:<br>
with open("arquivo1.txt","r+")as arquivo:<br>
arquivo.write("\nDécima linha do meu arquivo texto\n")<br>
arquivo.readline() (obs.: não esqueça da identação)<br>

<h1 align="center">Exercício:<h1>

### 1) Criando um arquivo de cadastro

arquivo = open("cadastro.txt","w")<br>
NOME = input('Nome: ')<br>
ENDER = input('Endereço: ')<br>
arquivo.write('Nome: ' + NOME + '\nEndereço: ' + ENDER)<br>
arquivo.close()<br>

### 2) Acrescentando dados no cadastro

arquivo = open("cadastro.txt","a")<br>
NOME = input('Nome: ')<br>
ENDER = input('Endereço: ')<br>
arquivo.write('\n\nNome: ' + NOME + '\nEndereço: ' + ENDER)<br>
arquivo.close()<br>

### 3) Criar um programa com menu para inclusão, leitura, acrescentar dados de alunos, contendo os campos : matricula, nome, nota1, nota 2 e média, utilizando a estrutura enquanto de repetição. Criar um módulo de leitura dos dados do arquivo.

      *****************************************
      ** CADASTRO DE ALUNOS **
      *****************************************

      Criar Arquivo ----- <1>
      Adicionar dados --- <2>
      Leitura ----------- <3>
      Sair -------------- <4>

      ********************************************
      ** Inclusão de Dados **
      ********************************************

      Matricula:
      Nome:
      Nota-1:
      Nota-2:
      Media:
      
      print("*****************************************")
      print("********** CADASTRO DE ALUNOS ***********")
      print("*****************************************")
      ESC = 0
      while ESC != 4:
              print("_________MENU__________")
              print("\nCriar Arquivo ----- <1>")
              print("Adicionar dados --- <2>")
              print("Leitura ----------- <3>")
              print("Sair -------------- <4>")
              print("_______________________")
              ESC = int(input ('Digite um procedimento do menu: . . .'))#QUANDO CRIA OS ARQUIVOS COM O MESMO NOME DE PASTA APAGA DADOS ANTERIORES
              if ESC == 1:
                      arquivo = open("arquivo1.txt","w")
                      arquivo.write("")
                      arquivo.close()
                      print("********************************************")
                      print("****** Arquivo Criado com Sucesso **********")
                      print("********************************************")
              elif ESC == 2:
                      FECHAR=0
                      while FECHAR != 1:
                              print("********************************************")
                              print("********** Inclusão de Dados ***************")
                              print("********************************************")
                              MATRICULA = input ('Digite sua matricula: . . .')
                              NOME = input ('Digite seu nome: . . .')
                              N1 = int(input ('Digite sua nota 1: . . .'))
                              N2 = int(input ('Digite sua nota 2: . . .'))
                              MEDIA = (N1+N2)/2
                              arquivo = open("arquivo1.txt","a")
                              arquivo.write("Nome: "+NOME+"    matricula:"+MATRICULA)
                              arquivo.write("\nnotas: {} e {}     media: {}\n\n".format(N1,N2,MEDIA))
                              arquivo.close()
                              FECHAR = int(input("Para voltar ao MENU digite(1) para outro cadastro digite (0)"))
              elif ESC == 3:
                      arquivo = open("arquivo1.txt","r")
                      print("-----------------------------------")
                      print (arquivo.read())
                      print("-----------------------------------")
                      arquivo.close()
              elif ESC == 4:
                      print("********************************************")
                      print("********** Processo Encerrado **************")
                      print("********************************************")

            

<h3>Atividade Autõnoma Aura:</h3>

1) A metodologia de desenvolvimento rápido de software (RAD) tem como objetivos a acelerar o processo de entrega de software através de um processo que prioreiza o desenvolvimento no curto prazo com entregas que incorporam conceitos bem debatidos com as partes envolvidas. Portanto a RAD possui vanatagens, em especial, em relação aos métodos tradicionais de desenvolvimento. Nesse sentido, selecione a opção que NÃO é uma vantagem de metodologia RAD.

a) Integração antecipada do sistema e redução de riscos<br> X
b) Adaptabilidade e compartimentação dos compenentes do sistema<br>
c) Versões iterativas e menor tempo de colocação no mercado<br>
d) Feedback constante do usuário<br>
e) Ter como pré-requisito equipes tecnicamentes muito qualificadas<br>


2)Para que o RAD posso comprir seu objetivo que é o de reduzir o tempo de entrega de produtos, ela precisa de ferramentas que facilitem o desenvolvimento de software . Um dos recursos meis importantes para atingir otal objetivo é ouso de fremeworks. Em relação  aos frameworks para desenvolvimento de aplicações RAD, selecione a opção CORRETA:

a) A escolha de um framework sempre deve levar em conideraçãoas necessidades do projeto que se deseja implementar, portanto essa escolha tem que estar baseada nas bibliotecas, documentação disponível e a linguagem de programação disponibilizadas para desenvolver o projeto. X
b) Independe da linguagem de programação escolhida é essencial que tenha copmo base o python por se tratar de uma linguagem moderna e bem documentada.
c) Atualmente, qualquer projeto precisa levar em consideração do modelo cliente-servidor,portanto a escolha do framework deve levar isso em consideração.
d) Qualquer projeto RAD implementado em Python deve utilizar frameworks Tkinter e Django.
e) A escolha de um framework não deve levar em consideração as nessecidades do projeto que se deseja implementar. Ela tem que estar em consideração as necessidades do projeto que se deseja implementar. Ela tem que estar baseada nas bibliotecas, documentação disponivel e a linguagem de programação disponibilizadas para desenvolver o projeto.










