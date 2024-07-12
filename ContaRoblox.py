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
            print(f"Foi acrescentado {valor} em quantidade de robux.")
            print("Foi creditado R$ %.2f em seu cartão"% (0.06975*valor))
        else:
            print("Erro na compra.")
    
    def AdicionarTix(self, valor):
        if valor > 0:
            self.tix += valor
            print(f"Foi acrescentado {self.tix} em quantidade de tickets.")
        else:
            print("Erro na aquisição.")

    def ConsultarInventario(self):
        print(self.Inventory)
    
    def Extrato(self):
        print(f"Nome: {self.nickname} | Tix: {self.tix} | Robux: {self.robux} | Conta premium: {self.IsPremium}")
    
    