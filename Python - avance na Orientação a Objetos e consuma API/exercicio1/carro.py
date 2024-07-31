from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        return super().__str__() + f' | Numero de portas: {str(self._portas).ljust(5)}'