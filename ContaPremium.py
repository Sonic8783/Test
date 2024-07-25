class Premium:
    def __init__(self):
        pass
    def PegarPremium(self, Conta):
        self.select = input("É necessário ter \033[32m2.900 robux\033[0m para tornar-se premium, deseja prosseguir? (s/n): ")
        if self.select == 's' and Conta.robux >= 2900 and Conta.IsPremium == False:
            Conta.robux -= 2900
            Conta.IsPremium = True
            print("Premium ativado com sucesso.")
        elif Conta.IsPremium == True:
            print("\033[31mErro:\033[0m Conta já possui premium.")
        else:
            print("\033[31mErro:\033[0m saldo insuficiente.")