class Carro:
    # Método construtor
    def __init__(self, marca, modelo, placa, valor):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.__valor = valor
        self.quilometragem = 0
        self.disponivel = True

    def exibir(self):
        print(f"{self.marca} - {self.modelo} - {self.placa} - {self.__valor} - {self.quilometragem} - {self.disponivel}")

    def alugar(self):
        if(self.disponivel == True):
           self.disponivel = False
           print ("O carro foi alugado com sucesso")
        else:
            print("O carro esta indisponivel")

    def devolver(self, novo_quilometragem):
        if(self.disponivel == False):
            if novo_quilometragem > self.quilometragem:
                self.disponivel = True
                print ("O carro foi devolvido com sucesso")
            else:
                print ("A quilometragem está errada")
        else: 
            print ("O carro já está disponivel")

#Quarto.   Carro
#id.    valor1
#tipo.     valor2
#valor.   valor3
#disponivel.     ativo
##devolver().   desativar()
#alugar()
#alterar_preco().   alterar_valor()


#exibir ()
#devolver()