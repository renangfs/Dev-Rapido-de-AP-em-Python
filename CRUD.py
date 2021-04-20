import mysql.connector
from mysql.connector import Error #importa a biblioteca de tratamento de erro
conn = mysql.connector.connect(host='localhost',database='bd',user='root',password='')# (conn)variavel global para conexão do banco de dados
#commit = so vai ser realmente gravada se acontecer um commit
op = 0
while(op != 5):#Estrutura de repetição 
    print("\n=========== Tabela do CRUD ============")
    print("Adicionar mais Informações ao Banco -- 1")
    print("Ler o Banco de Dados ----------------- 2")
    print("Alterar linha do banco --------------- 3")
    print("Exluir linha do banco ---------------- 4")
    print("Sair do programa --------------------- 5")
    print("=======================================\n")
    op = int(input("Digite uma operação..:"))

    if op == 1:#Adicionando registro no banco
        conn = mysql.connector.connect(host='localhost',database='bd',user='root',password='')#coloquei a conexão aqui para evitar erros
        try:#Tratamento de erro

            idpessoaa=(input("Digite seu id:..."))
            nomea=input("Digite seu nome:...")
            telefonea=input("Digite seu telefone:...")
            
            dados = idpessoaa+',\''+nomea+'\',\''+telefonea+'\')'#padrões (\'') para por aspa no inicio ('\')para por aspa no final
            #print (dados) ...ver as ordens dos dados

            comando="""INSERT INTO pessoa (id,nome,telefone) VALUES("""           
            sql = comando+dados   
                                            
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()#Salvando alterações

            print("\n***Registro INSERIDO com sucesso!!!***\n")
            print(cursor.rowcount,"Registros na tabela")#mostra a quantidade de registros na tabela
        except Error as erro:#Tratamento de erro
            print("Erro ao inserir dados na tebela",erro)
        finally:#fechando conexão
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("Conexão encerrada")
                MENU=(input("Pressione qualquer tecla para voltar ao menu...."))
                
    if op == 2:#lendo dados do banco
        conn = mysql.connector.connect(host='localhost',database='bd',user='root',password='')#coloquei a conexão aqui para evitar erros
        print("------------------------------------")
        print("Pesquisar por nome --------------- 1")
        print("Consultar todos os dados --------- 2")
        print("------------------------------------")
        option = int(input("\nSua opção: "))
        if option == 1:
            try:
                nomePesq = input("\nDigite o nome para pesquisa: ")#A consulta por nome não é case sensitive
                query = "SELECT * FROM pessoa WHERE nome = '{}'".format(nomePesq)#Nome para pesquisa no banco de dados

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
                    print("Telefone......: ",linha[2],"\n")
            except Error as erro:#Tratamento de erro
                print("Erro ao acessar o SGBD",erro)
            finally:#fechando conexão
                if conn.is_connected():
                    cursor.close()
                    conn.close()
                    print("Conexão encerrada")
                    MENU=(input("Pressione qualquer tecla para voltar ao menu...."))

        if option == 2:
            try:
                query = "SELECT * FROM pessoa" 
                cursor = conn.cursor()#apontador
                cursor.execute(query)#O cursor aponta para todas as respostar das execuções da query
                linhas = cursor.fetchall()#(fetchall)recebe todas as resposta da base de dados
                print("Numero total de registros retornados: ",cursor.rowcount)#conta os registros da consulta
                print("\n***Pessoas Cadastradas***\n")
                    
                linha = 0
                for linha in linhas: #cria uma estrutura de repatição que é apontada atraves dos vetores
                    print("Codigo........: ",linha[0])
                    print("Nome..........: ",linha[1])
                    print("Telefone......: ",linha[2],"\n")
                
            except Error as erro:#Tratamento de erro
                    print("Erro ao acessar o SGBD",erro)
            finally:#fechando conexão
                    if conn.is_connected():
                        cursor.close()
                        conn.close()
                        print("***Conexão Encerrada***") 
                        MENU=(input("Pressione qualquer tecla para voltar ao menu...."))

    if op == 3:#Alterando registro no banco
        conn = mysql.connector.connect(host='localhost',database='bd',user='root',password='')#coloquei a conexão aqui para evitar erros
        try:
            altid = input("Digite o ID para ser alterado: ")
            novonome = input("Digite o NOVO NOME: ")
            novotelefone = input("Digite o NOVO TELEFONE: ")

            alterar_dados = "UPDATE pessoa SET nome = '{}', telefone = '{}' WHERE id = '{}' ".format(novonome,novotelefone, altid)

            cursor = conn.cursor()
            cursor.execute(alterar_dados)
            conn.commit()
            print("\n***Registro ALTERADO com sucesso!!!***\n")
            print(cursor.rowcount,"Registros alterado na tabela")#mostra a quantidade de registros na tabela
        except Error as erro:
            print(erro)
        MENU=(input("Pressione qualquer tecla para voltar ao menu...."))

    if op == 4:
        conn = mysql.connector.connect(host='localhost',database='bd',user='root',password='')#coloquei a conexão aqui para evitar erros
        try:
            pesqId = input("Digite o ID para ser excluido: ")

            dell_dados = "DELETE FROM pessoa WHERE pessoa.id = {}".format(pesqId)
            
            cursor = conn.cursor()
            cursor.execute(dell_dados)
            conn.commit()
            print("\n***Registro EXCLUIDO com sucesso!!!***\n")
            print(cursor.rowcount,"Registros alterado na tabela")#mostra a quantidade de registros na tabela
        except Error as erro:
            print(erro)

        MENU=(input("Pressione qualquer tecla para voltar ao menu...."))
    if op == 5:
        print("********************************************")
        print("************ Fim do Programa ***************")
        print("********************************************")
