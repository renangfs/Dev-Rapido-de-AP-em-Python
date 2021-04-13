import mysql.connector#biblioteca para conectar o MySQL

conn = mysql.connector.connect(host='localhost',database='conexão',user='root',password='')#criando variavel de conexão ao banco de dados

if conn.is_connected():
    db_info = conn.get_server_info()#pegando a versão do banco de dados
    print("Conectado ao servidor MySQL versão",db_info)

    cursor = conn.cursor()#cursor = tupla
    cursor.execute("select database();")#executa o comandos
    linha = cursor.fetchone()#pega a consulta do comando executado BD
    print("Conectado ao Banco de dados",linha)#apresenta a consulta

if conn.is_connected():
    cursor.close()#limpando memoria do cursor
    conn.close()#fechando conexão ao banco de dados
    print("O Banco de dados",linha,"foi encerrado")

 
