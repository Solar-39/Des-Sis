class Exemplo:
    # Método construtor
    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.__valor3 = valor3
        self.ativo = True

    def exibir_detalhes(self):
        print(f"{self.valor1} - {self.valor2} - {self.__valor3} - {self.ativo}")

    def desativar(self):
        if self.ativo == True:
            self.ativo = False
            print("Agora está desativado.")
        else:
            print("Já está desativado.")

    def ativar(self):
        if self.ativo == False:
            self.ativo = True
            print("Agora está ativado.")
        else:
            print("Já está ativado.")

    def alterar_valor(self, novo_valor):
        self.__valor3 = novo_valor


#Quarto.    Exemplo
#id.    valor1
#tipo.     valor2
#valor.   valor3
#disponivel.     ativo
#reservar().   desativar()
#liberar().   ativar()
#alterar_preco().   alterar_valor()
