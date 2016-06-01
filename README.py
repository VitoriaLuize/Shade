#essa primeira parte esta pronta, a parte do login. please não toca. bjão de luz.
print("                  ⎝ ▲ Olá, Bem vindo ao ŠHɅDΣ ▲ ⎞                  ")
print("ᄽ O ŠHɅDΣ é uma ferramenta de auxilio ao grande e pequeno comerciante.\n Que facilita o entendimento de todo o seu estoque,preços e suas atualizações \n Deixando claro tudo o que você precisa para ter o controle do seu comercio.ᄿ")
cadastro=str.upper(input("                  「 JɅ ESTɅ CɅDɅSTRɅDO 」: ") )
if cadastro == "SIM":
    login=str.upper(input("ℒogin : "))
else:
    print("               │ VAMOS SE CɅDɅSTRɅR ? ┃")
    novo_cadastro=str.upper(input("DIGITE O LOGIN DESEJADO: "))
    print(" PRONTO.",novo_cadastro,"já foi cadastrado. Volte ao menu principal")
    login=str.upper(input("ℒogin : "))
if login!= "yeah":
    print("_____________________________________________________________")
    print("╳                     ✳   ŠHɅDΣ    ✳                       ╳")
    print("╳            ◄ ⎝ Ⅰ ⎞ CɅDɅSTRɅR PRθDƲTθ                       ╳")
    print("╳            ◄  ⎝ Ⅱ ⎞ PESɊƲISAR PRθDƲTθ                     ╳")
    print("╳            ◄   ⎝ Ⅲ ⎞ PESɊƲISAR PθR PREÇθ                   ╳")           
    print("╳            ◄    ⎝ Ⅳ ⎞ ESTOQUE TOTAL                       ╳")      
    print("╳            ◄     ⎝ Ⅴ ⎞ RETIRADA DE PRθDƲTθS                ╳")          
    print("╳            ◄      ⎝ Ⅵ ⎞ ESTOQUE ATUALIZADO                ╳")
    print("╳            ◄        ⎝ VII⎞ SAIR                            ╳")
    print("_____________________________________________________________")

print("                                                                             ")
print("                                                                             ")
print("                                                                             ")
print("                                                                             ")
print("                                                                             ")
print("                                                                             ")
print("                                                                             ")
print("                                                                             ")

# acaba aqui no momento

'''#opção ==1  
print("                 │   ✳   ŠHɅDΣ    ✳   │")                 
print("                 │  CɅDɅSTRɅR PRθDƲTθ  │")
print(str.upper(input(" │ QUANTOS PRODUTOS VÃO SER CADASTRADOS ? ")))
#for i in range
print(str.upper(input( "│ NθMΣ: ")))
print(str.upper(input( "│ QUANTIDADΣ: ")))
print(int(input(       "│ VALOR DO PRODUTO:R$ ")))

#opçao==2
print("                         │   ✳   ŠHɅDΣ    ✳    │")  
print("                         │   PESɊƲISAR PRθDƲTθ  │")
print(str.upper(input("         │  QUAL PRODUTO VOCÊ PROCURA? ")))

#opçao==3
print("          │   ✳   ŠHɅDΣ    ✳       │ ")
print("          │    PESɊƲISAR PθR PREÇθ  │ ")
print(int(input("│  QUAL O PREÇO QUE VOCÊ QUER? R$")))

#opçao==4
print("                    │   ✳   ŠHɅDΣ    ✳       │ ")
print("                    │    ESTOQUE TOTAL        │ ")
print(str.upper(input("    │ DESEJA EXIBIR TODO O ESTOQUE? ")))
print("│ESTOQUE TOTAL :")
    

#opção==5

print("                 │   ✳   ŠHɅDΣ    ✳       │ ")
print("                 │    RETIRADA DE PRθDƲTθS │ ")
print(int(input("       │QUANTOS PRODUTOS VÃO SER RETIRADOS? ")))
print(str.upper(input(" │ TEM CERTEZA QUE VAI QUERER RETIRAR ELES? ")))
#if
print("                 │ PRODUTOS RETIRADOS │")


#opção==6
print("    │   ✳   ŠHɅDΣ    ✳       │ ")
print("    │ ESTOQUE ATUALIZADO      │ ")
print(str.upper(input(" │ DESEJA EXIBIR O ATUAL ESTOQUE? ")))
print("│NOVO ESTOQUE: ")

#opção==7
print(" │ FOI UM PRAZER PARA NÓS, TER VOCÊ COMO USUARIO. ATÉ A PROXIMA VISITA. │")




