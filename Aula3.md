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

arquivo = open("cadastro.txt","w")
NOME = input('Nome: ')
ENDER = input('Endereço: ')
arquivo.write('Nome: ' + NOME + '\nEndereço: ' + ENDER)
arquivo.close()

### 2) Acrescentando dados no cadastro

arquivo = open("cadastro.txt","a")
NOME = input('Nome: ')
ENDER = input('Endereço: ')
arquivo.write('\n\nNome: ' + NOME + '\nEndereço: ' + ENDER)
arquivo.close()













