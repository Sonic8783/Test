from ContaRoblox import ContaRoblox
from NickRoblox import ContaNickname
from Catalogo import Catalog
from ContaPremium import Premium
print("\033[34mOlá! Seja bem-vindo ao ROBlOX!\033[0m")
Nick1 = ContaNickname(input("Para começarmos, digite o seu nickname: "))
Conta1 = ContaRoblox(Nick1.Get_Nickname())
print("Boas vindas ao ROBLOX, aqui está a sua conta:")
Conta1.Extrato()

while True:
    choice = 0
    print("Opções:\n1 - Comprar robux\n2 - Adquirir tickets\n3 - Abrir catálogo\n4 - Tornar-se premium\n5 - Inventário\n6 - Consultar extrato")
    choice = int(input())
    if choice == 1:
        Conta1.ComprarRobux(int(input("Digite o valor que deseja comprar: \033[32m")))
    elif choice == 2:
        Conta1.AdicionarTix(int(input("Digite a quantidade que deseja adicionar: \033[33m")))
    elif choice == 3:
        Catalog().ComprarChapéu(Conta1) #Chama o ComprarChapéu onde é colocado o objeto que já tem os atributos Conta.robux (no código Catálogo.py) que pode ser alterável
    elif choice == 4:
        Premium().PegarPremium(Conta1)
    elif choice == 5:
        Conta1.ConsultarInventario()
    elif choice == 6:
        Conta1.Extrato()
    else:
        print("Erro: opção inválida")