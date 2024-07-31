class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    def __str__(self):
        return f'Marca: {self._marca.ljust(20)} | Modelo: {self._modelo.ljust(20)} | Estado: {self.ligado.ljust(10)}'
    
    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'
    

