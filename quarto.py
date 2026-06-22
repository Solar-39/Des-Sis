class Quarto:
# metodo construtor
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.__valor = valor
        self.disponivel = True

    def exibir_detalhes(self):
        print (f"quarto" {self.id} - {self.tipo} - {self.__valor} - {self.disponivel})

    def reservar(self):
        if(self.disponivel == True)
           self.disponivel = False
           print ("O quarto foi reservado com sucesso")
        else:
            print("o quarto esta indisponivel")


    def liberar(self)
        if(self.disponivel == False)
           self.disponivel = True
           print ("O quarto foi liberado com sucesso")
        else:
            print("o quarto esta disponivel")

    def alterar_preco(self, novo_valor):
        self.__valor = novo_valor

