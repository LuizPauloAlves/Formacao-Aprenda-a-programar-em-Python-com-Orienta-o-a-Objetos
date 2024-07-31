from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def __str__(self):
        return super().__str__() + f' | Cor do carro: {self._cor.ljust(20)}'
    
    def ligar(self):
        pass