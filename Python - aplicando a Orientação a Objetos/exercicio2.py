class Musica:
    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

# 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_1 = Carro('Uno', 'Branco', '1998')

# 2(classe), 3(instancia usando o contrutor) e 4(__str__)
class Restautante:
    def __init__(self, nome, categoria, endereco, avaliacao_media = 0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = endereco
        self.avaliacao_media = avaliacao_media

    def __str__(self):
        status = "Aberto" if self.ativo else "Fechado"
        return (f'''Nome: {self.nome}
                Categoria: {self.categoria}
                Status:{status}
                Endereço: {self.endereco}
                Avaliação Média: {self.avaliacao_media}''')

restaurante_1 = Restautante('Cozinha Italiana','Italiana','Rua Mamamia Corleone', 5)
print(restaurante_1)

# 5
class Cliente:
    def __init__(self, nome, idade, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.enderco = endereco

cliente_1 = Cliente('Joao', 20,'12 9 8765-4321','Rua do Joao')
cliente_2 = Cliente('Gabriel', 21,'12 9 8765-4321','Rua do Gabriel')
cliente_3 = Cliente('Luiz', 22,'12 9 8765-4321','Rua do Luiz')