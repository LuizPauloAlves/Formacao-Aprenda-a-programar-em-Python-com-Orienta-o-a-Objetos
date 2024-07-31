from modelos.restaurantes import Restaurante

restaurante_1 = Restaurante('mamamia','italiana')
restaurante_2 = Restaurante('Sushi Zen','Japonesa')
restaurante_3 = Restaurante('Churras Do Papa', 'brasileira')

restaurante_1.receber_avaliacao('Gui', 5)
restaurante_1.receber_avaliacao('Lais', 4)
restaurante_1.receber_avaliacao('Emy', 2)

restaurante_2.alterar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()