#Teste
#Teste 2
#Teste
#Teste 2
from ContaRoblox import ContaRoblox
class Catalog(ContaRoblox):
    def __init__(self):
        self.opcao = None
        self.chapeus_robux = {
            1: {'1. Boné - 10 Robux': 10}, 2: {'2. Touca - 20 Robux': 20}, 3: {'3. Óculos Escuros - 15 Robux': 15}, 4: {'4. Mochila - 25 Robux': 25},
            5: {'5. Jaqueta - 30 Robux': 30}, 6: {'6. Calça Jeans - 20 Robux': 20}, 7: {'7. Tênis - 35 Robux': 35}, 8: {'8. Relógio - 40 Robux': 40},
            9: {'9. Anel - 50 Robux': 50}, 10: {'10. Brinco - 15 Robux': 15}, 11: {'11. Colar - 25 Robux': 25}, 12: {'12. Pulseira - 20 Robux': 20},
            13: {'13. Chapéu de Cowboy - 30 Robux': 30}, 14: {'14. Cinto - 10 Robux': 10}, 15: {'15. Luvas - 15 Robux': 15}, 16: {'16. Cachecol - 20 Robux': 20},
            17: {'17. Camiseta - 10 Robux': 10}, 18: {'18. Bermuda - 15 Robux': 15}, 19: {'19. Sapato Social - 40 Robux': 40}, 20: {'20. Meias - 5 Robux': 5},
            21: {'21. Jaqueta de Couro - 50 Robux': 50}, 22: {'22. Óculos de Sol - 20 Robux': 20}, 23: {'23. Chapéu de Palha - 15 Robux': 15},
            24: {'24. Camisa Polo - 25 Robux': 25}, 25: {'25. Calça Social - 30 Robux': 30}, 26: {'26. Sapato Esportivo - 35 Robux': 35},
            27: {'27. Moletom - 20 Robux': 20}
        }
        
        self.chapeus_tix = {
            30: {'30. Camisa Legal - 15 Tix': 15}, 31: {'31. Cabelo Legal - 75 Tix': 75}, 32: {'32. Jaqueta Jeans - 50 Tix': 50}, 33: {'33. Calça Cargo - 40 Tix': 40},
            34: {'34. Botas - 60 Tix': 60}, 35: {'35. Boné de Aba Reta - 20 Tix': 20}, 36: {'36. Camiseta Estampada - 25 Tix': 25}, 37: {'37. Shorts - 15 Tix': 15},
            38: {'38. Sandálias - 10 Tix': 10}, 39: {'39. Óculos de Grau - 30 Tix': 30}, 40: {'40. Relógio de Pulso - 45 Tix': 45}, 41: {'41. Brincos de Argola - 20 Tix': 20},
            42: {'42. Colar de Pérolas - 35 Tix': 35}, 43: {'43. Pulseira de Couro - 25 Tix': 25}, 44: {'44. Chapéu de Pescador - 15 Tix': 15},
            45: {'45. Cinto de Couro - 20 Tix': 20}, 46: {'46. Luvas de Inverno - 30 Tix': 30}, 47: {'47. Cachecol de Lã - 25 Tix': 25},
            48: {'48. Camiseta Regata - 10 Tix': 10}, 49: {'49. Bermuda de Praia - 20 Tix': 20}, 50: {'50. Sapato de Couro - 50 Tix': 50},
            51: {'51. Meias Coloridas - 5 Tix': 5}, 52: {'52. Jaqueta de Nylon - 40 Tix': 40}, 53: {'53. Óculos de Leitura - 20 Tix': 20},
            54: {'54. Chapéu de Festa - 15 Tix': 15}, 55: {'55. Camisa Social - 30 Tix': 30}, 56: {'56. Calça de Sarja - 35 Tix': 35},
            57: {'57. Tênis de Corrida - 45 Tix': 45}, 58: {'58. Moletom com Capuz - 25 Tix': 25}, 59: {'59. Camiseta de Time - 20 Tix': 20},
            60: {'60. Calça de Moletom - 30 Tix': 30}, 61: {'61. Sapato de Salto - 50 Tix': 50}, 62: {'62. Meias de Algodão - 10 Tix': 10},
            63: {'63. Jaqueta de Esqui - 60 Tix': 60}, 64: {'64. Óculos de Proteção - 25 Tix': 25}, 65: {'65. Chapéu de Copa Alta - 20 Tix': 20},
            66: {'66. Camisa de Manga Longa - 25 Tix': 25}, 67: {'67. Calça de Treino - 35 Tix': 35}, 68: {'68. Tênis de Basquete - 50 Tix': 50},
            69: {'69. Moletom sem Capuz - 20 Tix': 20}, 70: {'70. Camiseta de Malha - 15 Tix': 15}, 71: {'71. Calça de Algodão - 25 Tix': 25},
            72: {'72. Sapato de Cano Alto - 40 Tix': 40}, 73: {'73. Meias de Lã - 15 Tix': 15}, 74: {'74. Jaqueta de Couro Sintético - 50 Tix': 50},
            75: {'75. Óculos de Sol Espelhado - 30 Tix': 30}, 76: {'76. Chapéu de Palha Grande - 20 Tix': 20}, 77: {'77. Camisa de Linho - 35 Tix': 35},
            78: {'78. Calça de Linho - 40 Tix': 40}, 79: {'79. Tênis de Tênis - 45 Tix': 45}, 80: {'80. Moletom com Zíper - 25 Tix': 25},
            81: {'81. Camiseta de Algodão - 10 Tix': 10}, 82: {'82. Calça de Pijama - 20 Tix': 20}, 83: {'83. Sapato de Veludo - 50 Tix': 50},
            84: {'84. Meias de Seda - 15 Tix': 15}, 85: {'85. Jaqueta de Pelúcia - 60 Tix': 60}, 86: {'86. Óculos de Sol Redondo - 25 Tix': 25},
            87: {'87. Chapéu de Copa Baixa - 15 Tix': 15}
        }
        self.bone = 10
        self.touca = 20
    
    def ComprarChapéu(self, Conta): #Selecione a conta que deseja comprar o chapéu, pega seus atributos
        self.robux = Conta.robux #Chama o atributo do objeto
        self.tix = Conta.tix #Chama o atributo do objeto
        for p_id, p_info, in (self.chapeus_robux.items()): #p_id é o id da variável, p_info é as informações dentro dessa variável
            for i in p_info :
                print(i) #p_info[i] = informacoes dentro de cada variavel, i = informações sobre cada variável
        for p_id, p_info, in (self.chapeus_tix.items()):
            for i in p_info:
                print(i) #Imprime a lista com as keys somente
        self.opcao = int(input())
        
        if self.opcao in (self.chapeus_robux):
            self.produto_robux = list(self.chapeus_robux[self.opcao].values())[0] #Em forma de lista, é pego o valor do dicionário o elemento 0
            
            if (self.robux >= (self.produto_robux)):
                Conta.robux -= self.produto_robux #Subtrai 10 do atributo 'robux' do objeto
                print("Compra realizada com sucesso.")
                Conta.Inventory.append(list(self.chapeus_robux[self.opcao].items())[0][0])
            else:
                print("Erro: saldo insuficiente")
        elif self.opcao in (self.chapeus_tix):    
            self.produto_tix = list(self.chapeus_tix[self.opcao].values())[0]
            if(self.tix >= (self.produto_tix)): #Praticamente Conta.tix, mas facilia a assossiação
                Conta.tix -= self.produto_tix #Subtrai 10 do atributo 'robux' do objeto
                print("Compra realizada com sucesso.")
                Conta.Inventory.append(list(self.chapeus_tix[self.opcao].items())[0][0])
            else:
                print("Erro: saldo insuficiente")
        
        else:
            print("Erro: item não encontrado")