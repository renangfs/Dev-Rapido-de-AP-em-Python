# programa para ler os dados da base de dados já armazenados
import mysql.connector
from mysql.connector import Error#importa a biblioteca de tratamento de erro

try:#Tratamento de erro
    conn = mysql.connector.connect(host='localhost',database='conexão',user='root',password='')#criando variavel de conexão ao banco de dados
    #nome="'renan'"
    query = "SELECT * FROM pessoa"# WHERE nome = {}.format(nome) # teste....(SELECT * FROM pessoa WHERE nome = "renan")

    cursor = conn.cursor()#apontador
    cursor.execute(query)#O cursor aponta para todas as respostar das execuções da query
    linhas = cursor.fetchall()#(fetchall)recebe todas as resposta da base de dados
    print("Numero total de registros retornados: ",cursor.rowcount)#conta os registros da consulta

    print("\nPRODUTOS CADASTRADOS")
    print("\n======== ===========\n\n")
    linha = 0
    for linha in linhas: #cria uma estrutura de repatição que é apontada atraves dos vetores
        print("Codigo........: ",linha[0])
        print("Nome..........: ",linha[1])
        print("Telefone......: ",linha[2])
        print("Endereco......: ",linha[3],"\n")
except Error as erro:#Tratamento de erro
    print("Erro ao acessar o SGBD",erro)
finally:#fechando conexão
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada")
