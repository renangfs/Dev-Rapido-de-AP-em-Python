#programa para inserir daos na base da tabela
import mysql.connector
from mysql.connector import Error#importa a biblioteca de tratamento de erro
#commit = Salvar permanentemente um conjunto de altereções
try:#Tratamento de erro
    conn = mysql.connector.connect(host='localhost',database='conexão',user='root',password='')#criando variavel de conexão ao banco de dados
    inserir_dados = """INSERT INTO pessoa (idpessoa,nome,telefone,endereco) VALUES (7,'Reinan','(21)90028922','Rua_TAL')"""

    cursor = conn.cursor()#aponta a query
    cursor.execute(inserir_dados)#executa a query
    conn.commit()#salva alterações (guarda)

    print("Registro inserido com sucesso!!!\n")
    print(cursor.rowcount,"Registros na tabela")
except Error as erro:#Tratamento de erro
    print("Erro ao inserir dados na tebela",erro)
finally:#fechando conexão
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada")
