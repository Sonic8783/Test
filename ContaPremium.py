class Premium:
    def __init__(self):
        pass
    def PegarPremium(self, Conta):
        self.select = input("É necessário ter 2.900 robux para tornar-se premium, deseja prosseguir? (s/n): ")
        if self.select == 's' and Conta.robux >= 2900 and Conta.IsPremium == False:
            Conta.robux -= 2900
            Conta.IsPremium = True
            print("Premium ativado com sucesso.")
        elif Conta.IsPremium == True:
            print("Erro: Conta já possui premium.")
        else:
            print("Erro: saldo insuficiente.")