def casdastrarProduto():
    arquivo = open("produtos.txt","a")
    print("◄ CɅDɅSTRɅR PRθDƲTθ")
    codigo=input("Digite um CθDIGθ: ")
    while(codigo+"\n" in criaListaArquivo()):
        print("Esse código já está cadastrado !")
        codigo=input("Digite umm novo CθDIGθ: ")
    nome_produto=str.upper(input( "NθMΣ: "))
    quantidade=int(input( "QUANTIDADΣ: "))
    preco=float(input(       "VALOR DO PRODUTO:R$ "))
    arquivo.writelines([codigo+"\n", nome_produto+"\n",str(quantidade)+"\n",str(preco)+"\n"])
    arquivo.close()

def criaListaArquivo():
    arquivo = open("produtos.txt","r")
    produtos = arquivo.readlines()
    arquivo.close()
    return produtos
        
def consultarProduto():
    codigo=input("PESQUISE O PRODUTO POR CÓDIGO: ")
    produtos = criaListaArquivo()
    for i in range(0,len(produtos),4):
        if(produtos[i] == codigo+"\n"):
            print("Código: ", produtos[i][:len(produtos[i])-1])
            print("Descrição: ", produtos[i+1][:len(produtos[i+1])-1])
            print("Quantidade: ", produtos[i+2][:len(produtos[i+2])-1])
            print("Preço: ", produtos[i+3][:len(produtos[i+3])-1])
            break

def listarEstoque():
    produtos = criaListaArquivo()
    for i in range(0,len(produtos),4):
        print("Código: ", produtos[i][:len(produtos[i])-1])
        print("Descrição: ", produtos[i+1][:len(produtos[i+1])-1])
        print("Quantidade: ", produtos[i+2][:len(produtos[i+2])-1])
        print("Preço: ", produtos[i+3][:len(produtos[i+3])-1]+"\n")

def alterarProdutoPorCodigo():
    produtos = criaListaArquivo()

    print("◄ ALTERAR PRθDƲTθ")
    codigo = input("DIGITE O CODIGO DO PRODUTO QUE DESEJA ALTERAR: ")

    for i in range(0,len(produtos),4):
        if (int(produtos[i]) == int(codigo)):
            novocodigo = input("NOVO CODIGO:")+"\n"
            produtos[i] = novocodigo
            produtos[i+1] = str.upper(input( "NOVO NθMΣ: "))+"\n"
            produtos[i+2] = input( "NOVA QUANTIDADΣ: ")+"\n"
            produtos[i+3] = input("NOVO VALOR DO PRODUTO:R$ ")+"\n"
            arquivo = open("produtos.txt","w")
            arquivo.writelines(produtos)
            arquivo.close()
            break
     
def cls():
    for i in range(50):
        print()
        
def apagarProduto():
    produtos = criaListaArquivo()
    print("◄ APAGAR PRθDƲTθ")
    codigo = input("DIGITE O CODIGO DO PRODUTO QUE DESEJA APAGAR: ")
    
    for i in range(0,len(produtos),4):
        if (int(produtos[i]) == int(codigo)):
            del produtos[i]
            del produtos[i]
            del produtos[i]
            del produtos[i]
            arquivo = open("produtos.txt","w")
            arquivo.writelines(produtos)
            arquivo.close()
            break
