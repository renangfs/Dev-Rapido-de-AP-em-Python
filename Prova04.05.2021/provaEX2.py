cod = int(input("Digite o CODIGO do produto:..."))
nome = input("Digite o NOME do produto:...")
qtd = int(input("Digite o QUANTIDADE do produto:..."))
valc = float(input("Digite o VALOR do produto:..."))
valv = valc+((valc/100)*20)

arquivo = open("materiaisEstoque","w")
arquivo.write("\n\nCODIGO: {}              NOME: {}\n".format(cod,nome))
arquivo.write("QUANTIDADE: {}\n".format(qtd))
arquivo.write("Valor de compra: {:.2f}     Valor para Venda: {:.2f}\n".format(valc,valv))
arquivo.close()

arquivo = open("materiaisEstoque","r")
print (arquivo.read())
arquivo.close()