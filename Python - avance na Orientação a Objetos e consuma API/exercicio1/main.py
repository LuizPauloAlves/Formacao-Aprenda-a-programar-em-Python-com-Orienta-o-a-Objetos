from carro import Carro
from moto import Moto

def main():
    # Criando três instâncias de Carro
    carro1 = Carro("Toyota", "Corolla", 4)
    carro2 = Carro("Honda", "Civic", 4)
    carro3 = Carro("Ford", "Mustang", 2)

    # Criando três instâncias de Moto
    moto1 = Moto("Yamaha", "YZF-R1", "Esportiva")
    moto2 = Moto("Harley-Davidson", "Street 750", "Casual")
    moto3 = Moto("Ducati", "Panigale V4", "Esportiva")

    print(carro1)
    print(carro2)
    print(carro3)

    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == '__main__':
    main()