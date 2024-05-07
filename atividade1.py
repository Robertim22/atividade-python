class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)

meu_carro = Carro("Volkswagem", "Gol Quadrado")
meu_carro.exibir_informacoes()
