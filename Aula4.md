30/03/2021

link: https://web.microsoftstream.com/video/7d26207e-f8a9-409d-b1e0-d6455195b453
- toda linguagem consegue abrir arquivo txt
- arquivo TXT e compativel com todos dancos de dados
<h2 align="center"> Tratamento de erro com Python </h2>
<img src="https://user-images.githubusercontent.com/61218420/113019629-32c73e00-9158-11eb-9cf6-10ae9991cb5a.png" width="900">
  
    print("=================\n")
    print("Tabela de cadastro")
    print("==================\n")
    op = 0
    while(op != 4):#Estrutura de repetição 
        print("Criar um arquivo ------ 1")
        print("Adicionar mais Dados -- 2")
        print("Ler o programa -------- 3")
        print("Finalizar o programa -- 4")
        op = int(input("Digite um número..:"))

        if op == 1:#Cria um arquivo sem nenhum conteudo dentro OBS: se já existir um arquivo com conteudo será perdido
            arquivo= open ("cadastro1.txt", "w")
            arquivo.write("")
            arquivo.close()
            print("\n\n****Arquivo Criado com sucesso!****\n\n")

        if op == 2:#Esta condição cria um arquivo e acrescenta um novo arquivo caso ja exista sem apagar o conteudo
            arquivo= open ("cadastro1.txt", "a")
            print("Matricula:")
            mat = str(input("Sua matricula..:"))
            print("Nome")
            nome = str(input("Seu nome..:"))
            print("Nota 1")
            nota1 = float(input(""))
            print("Nota 2")
            nota2 = float(input(""))
            media = (nota1 + nota2) / 2
            print(media)
            arquivo.write("\nNome: " + nome + "\nMatricula: " + mat)
            arquivo.write("\nNotas {} e {} media:{}\n\n".format(nota1,nota2,media))
            arquivo.close()
            print("********************************************")
            print("*********** Dados Cadastrados **************")
            print("********************************************")
        if op == 3:
            try:
                arquivo= open ("cadastro1.txt","r")
                print("-----------------------------------")
                print (arquivo.read())
                print("-----------------------------------")
                arquivo.close()
            except FileNotFoundError as erro:
                print("-----------------------------------")
                print("Arquivo Inexistente !!!")
                print("Descrição: ",erro)
                print("Término do programa")
                print("-----------------------------------")

        elif op == 4:#Opção de saida para estrutura while While
            print("********************************************")
            print("********** Processo Encerrado **************")
            print("********************************************")



