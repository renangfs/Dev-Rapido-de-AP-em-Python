#programa para inserir dados na base da tabela
import mysql.connector
from mysql.connector import Error#importa a biblioteca de tratamento de erro
#commit = so vai ser realmente gravada se acontecer um commit
try:#Tratamento de erro
    conn = mysql.connector.connect(host='localhost',database='conexão',user='root',password='')

    idpessoaa=(input("Digite seu id:..."))
    nomea=input("Digite seu nome:...")
    telefonea=input("Digite seu telefone:...")
    enderecoa=input("Digite seu endereco:...")

    dados = idpessoaa+',\''+nomea+'\',\''+telefonea+'\',\''+enderecoa+'\')'#padrões (\'') para por aspa no inicio ('\')para por aspa no final
    print (dados)

    comando="""INSERT INTO pessoa (idpessoa,nome,telefone,endereco) VALUES("""           
    sql = comando+dados   
                                    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    print("Registro inserido com sucesso!!!\n")
    print(cursor.rowcount,"Registros na tabela")
except Error as erro:#Tratamento de erro
    print("Erro ao inserir dados na tebela",erro)
finally:#fechando conexão
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada")
