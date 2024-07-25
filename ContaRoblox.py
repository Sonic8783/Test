class ContaRoblox:
    def __init__(self, nickname):
        self.nickname = nickname
        self.IsPremium = False
        self.robux = 0
        self.tix = 0
        self.Inventory = []
        
    def Get_Robux(self):
        return self.robux
    def Set_Robux(self, valor):
        self.robux = valor
    def Get_Tix(self):
        return self.tix
    def Set_Tix(self, valor):
        self.tix = valor
    
    def ComprarRobux(self, valor):
        if valor > 0:
            self.robux += valor
            print(f"Foi acrescentado \033[32m{valor}\033[0m em quantidade de robux.")
            print("Foi creditado \033[32mR$ %.2f\033[0m em seu cartão"% (0.06975*valor))
        else:
            print("Erro na compra.")
    
    def AdicionarTix(self, valor):
        if valor > 0:
            self.tix += valor
            print(f"Foi acrescentado \033[33m{self.tix}\033[0m em quantidade de tickets.")
        else:
            print("Erro na aquisição.")

    def ConsultarInventario(self):
        print(self.Inventory)
    
    def Extrato(self):
        if self.IsPremium == True:
            print(f"{self.nickname} | \033[33mTix: {self.tix}\033[0m | \033[32mRobux (R$): {self.robux}\033[0m | \033[34mConta premium: {self.IsPremium}\033[0m")
        else:
            print(f"{self.nickname} | \033[33mTix: {self.tix}\033[0m | \033[32mRobux (R$): {self.robux}\033[0m | \033[31mConta premium: {self.IsPremium}\033[0m")
    
    