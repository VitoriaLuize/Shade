def casdastrarProduto():
    arquivo = open("produtos.txt","a")
    print("                   ▉CɅDɅSTRɅR PRθDƲTθ▉")
    codigo=input(" ▉ Digite um CθDIGθ(ex.00000): ")
    while(codigo+"\n" in criaListaArquivo()):
        print(" ▉Esse código já está cadastrado ! ▉")
        codigo=input(" ▉Digite um novo CθDIGθ(ex.00000): ")

    nome_produto=str.upper(input( " ▉NθMΣ: "))
    quantidade=int(input( " ▉QUANTIDADΣ: "))
    preco=float(input(       " ▉VALOR DO PRODUTO:R$ "))
    print("                   ▉PRODUTO CADASTRADO COM SUCESSO ▉")
    arquivo.writelines([codigo+"\n", nome_produto+"\n",str(quantidade)+"\n",str(preco)+"\n"])
    arquivo.close()

def criaListaArquivo():
    arquivo = open("produtos.txt","r")
    produtos = arquivo.readlines()
    arquivo.close()
    return produtos
        
def consultarProduto():
    achou = False
    codigo=input(" ▉PESQUISE O PRODUTO POR CÓDIGO ▉: ")
    produtos = criaListaArquivo()
    for i in range(0,len(produtos),4):
        if(produtos[i] == codigo+"\n"):
            print(" ▉Código: ", produtos[i][:len(produtos[i])-1])
            print(" ▉Descrição: ", produtos[i+1][:len(produtos[i+1])-1])
            print(" ▉Quantidade: ", produtos[i+2][:len(produtos[i+2])-1])
            print(" ▉Preço:R$ ", produtos[i+3][:len(produtos[i+3])-1])
            achou = True
            break
    if(achou == False):
        print("               ▉PRODUTO NÃO ENCONTRADO ▉ ")
        

def listarEstoque():
    produtos = criaListaArquivo()
    for i in range(0,len(produtos),4):
        print(" ▉Código: ", produtos[i][:len(produtos[i])-1],"▉")
        print(" ▉Descrição: ", produtos[i+1][:len(produtos[i+1])-1],"▉")
        print(" ▉Quantidade: ", produtos[i+2][:len(produtos[i+2])-1],"▉")
        print(" ▉Preço:R$ ", produtos[i+3][:len(produtos[i+3])-1]+"\n")
    if(len(produtos)==0):
        print("               ▉NENHUM PRODUTO CADASTRADO.DIGITE (1) PARA CADASTRAR ▉")

def alterarProdutoPorCodigo():
    produtos = criaListaArquivo()
    achou= False

    print("          ▉ALTERAR PRθDƲTθ ▉")
    codigo = input(" ▉DIGITE O CODIGO DO PRODUTO QUE DESEJA ALTERAR ▉: ")

    for i in range(0,len(produtos),4):
        if (int(produtos[i][:len(produtos[i])-1]) == int(codigo)):
            novocodigo = input(" ▉NOVO CODIGO:")+"\n"
            produtos[i] = novocodigo
            produtos[i+1] = str.upper(input( " ▉NOVO NθMΣ: "))+"\n"
            produtos[i+2] = input( " ▉NOVA QUANTIDADΣ: ")+"\n"
            produtos[i+3] = input(" ▉NOVO VALOR DO PRODUTO:R$ ")+"\n"
            arquivo = open("produtos.txt","w")
            arquivo.writelines(produtos)
            arquivo.close()
            acho=True
            break
    if(achou== False):
        print("                     ▉PRODUTO ALTERADO ▉")
     
def cls():
    for i in range(50):
        print()
        
def apagarProduto():
    produtos = criaListaArquivo()
    achou=False
    print(" ▉REMOVER PRθDƲTθ ▉")
    codigo = input(" ▉DIGITE O CODIGO DO PRODUTO QUE DESEJA REMOVER ▉: ")
    
    for i in range(0,len(produtos),4):
        if (int(produtos[i]) == int(codigo)):
            del produtos[i]
            del produtos[i]
            del produtos[i]
            del produtos[i]
            print("           ▉PRODUTO REMOVIDO COM SUCESSO ▉")
            arquivo = open("produtos.txt","w")
            arquivo.writelines(produtos)
            arquivo.close()
            achou=True
            break
    if(achou==False):
        print("               ▉PRODUTO NÃO ENCONTRADO ▉")
def sobreNos():
    print("                      │ Olá, Seja Bem-vindo ao  ŠHɅDΣ   ")
    print("                      │          ▉SOBRE NÓS ▉                            ")
    print("│O ŠHɅDΣ é uma ferramenta de auxilio ao grande e pequeno comerciante.          │")
    print("│Que facilita o entendimento de todo o seu estoque,preços e suas atualizações  │")
    print("│Deixando claro tudo o que você precisa para ter o controle do seu comercio.   │")





   
