#essa primeira parte esta pronta, a parte do login. please não toca. bjão de luz.
import arquivar



def menu():
    print("_____________________________________________________________")
    print("╳                     ✳   ŠHɅDΣ    ✳                       ╳")
    print("╳            ◄ ⎝ Ⅰ ⎞ CɅDɅSTRɅR PRθDƲTθ                      ╳")
    print("╳            ◄  ⎝ Ⅱ ⎞ RETIRADA DE PRθDƲTθS                  ╳")
    print("╳            ◄   ⎝ Ⅲ ⎞ PESɊƲISAR PθR PREÇθ                  ╳")           
    print("╳            ◄    ⎝ Ⅳ ⎞ ESTOQUE TOTAL                       ╳")      
    print("╳            ◄     ⎝ Ⅴ ⎞  PESɊƲISAR PRθDƲTθ                 ╳")          
    print("╳            ◄      ⎝ Ⅵ ⎞ SAIR                              ╳")
    print("_____________________________________________________________")

def casdastrarProduto():
    produto=[]
    print("                 │   ✳   ŠHɅDΣ    ✳   │")                 
    print("                 │  CɅDɅSTRɅR PRθDƲTθ  │")
    nome_produto=str.upper(input( "│ NθMΣ: "))
    quantidade=int(input( "│ QUANTIDADΣ: "))
    preco=int(input(       "│ VALOR DO PRODUTO:R$ "))
    codigo=int(input("       │ CθDIGθ: "))
    produto=nome_produto,quantidade,preco,codigo
    return produto

def apagarProduto(nome,num,produtos):
    lista = []
    lista = arquivar.apagarNome(nome,num,produtos)
    return lista
    
    
      
menu()
produtos = []
produtos = arquivar.ler()
produto = []
continuar=True
while continuar:
    opcao=str.upper(input("  │ DIGITE SUA OPÇÃO:  │"))
    if (opcao=="1"):
        arquivar.armazenar(casdastrarProduto())
    elif (opcao=="2"):
        print(" │ DESEJA RETIRAR POR NOME OU CODIGO? ")
        print("     │ DIGITE 1 PARA NOME. │              ")
        print("     │ DIGITE 2 PARA CODIGO│              ")
        ask = input()
        if (ask=="1"):
            produtos = arquivar.ler()
            nome=str.upper(input("│ DIGITE O NOME DO PRODUTO: "))
            arquivar.atualizarProdutos(apagarProduto(nome,0,produtos))              
        elif (ask=="2"):
            produtos = arquivar.ler()
            codigo=int(input("│ DIGITE O NOME DO PRODUTO: "))
            arquivar.atualizarProdutos(apagarProduto(codigo,3,produtos))  
