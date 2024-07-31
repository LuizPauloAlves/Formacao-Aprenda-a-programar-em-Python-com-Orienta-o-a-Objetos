# Classe Musica: Representa uma música com atributos de nome, artista e duração
# Definição da classe 'Musica'
class Musica:
    # Atributos da classe inicializados como strings vazias ou tipo inteiro
    nome = ''
    artista = ''
    duracao = int
# Cria uma instância da classe Musica e define seus atributos
musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355  # duração em segundos
# Cria outra instância da classe Musica com diferentes atributos
musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183  # duração em segundos
# Cria uma terceira instância da classe Musica com outros atributos
musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234  # duração em segundos



# Bloco 1: Definição e uso da classe Restaurante
# Definição da classe 'Restaurante'
class Restaurante:
    # Atributos da classe inicializados com valores padrão
    nome = ''
    categoria = ''
    ativo = False  # Indica se o restaurante está ativo ou não
# Cria uma instância da classe Restaurante e define o atributo 'categoria'
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'



# Bloco 2: Definir e acessar o atributo 'nome' da instância de Restaurante
# Define o nome do restaurante 'restaurante_praca'
restaurante_praca.nome = 'Praça'
# Armazena o nome do restaurante em uma variável
nome_do_restaurante = restaurante_praca.nome
# Imprime o nome do restaurante
print(nome_do_restaurante)



# Bloco 3: Verificar o estado (ativo ou inativo) de um restaurante
# Comentado o código que ativa o restaurante para manter o exemplo de estado inativo
# restaurante_praca.ativo = True
# Acessa o estado de atividade do restaurante e armazena em uma variável
estado_do_restaurante = restaurante_praca.ativo
# Verifica se o restaurante está ativo ou inativo e imprime uma mensagem correspondente
if estado_do_restaurante:
    print('Restaurante está ativo')
else:
    print('Restaurante está inativo')



# Bloco 4: Acessar o atributo 'categoria' da classe Restaurante
# Acessa a categoria padrão da classe 'Restaurante' (não das instâncias)
categoria = Restaurante.categoria



# Bloco 5: Criar uma nova instância de Restaurante e definir seu nome
# Cria uma nova instância da classe Restaurante chamada 'restaurante_bistro'
restaurante_bistro = Restaurante()
# Define o nome do 'restaurante_bistro'
restaurante_bistro.nome = 'Bistrô'
# Imprime o nome do 'restaurante_bistro'
print(restaurante_bistro.nome)



# Bloco 6: Criar uma outra instância de Restaurante e definir seus atributos
# Cria uma nova instância da classe Restaurante chamada 'restaurante_pizza'
restaurante_pizza = Restaurante()
# Define o nome e a categoria do 'restaurante_pizza'
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'



# Bloco 7: Verificar a categoria de um restaurante
# Verifica se a categoria do 'restaurante_pizza' é 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    # Se for 'Fast Food', imprime uma mensagem correspondente
    print('A categoria é Fast Food.')
else:
    # Caso contrário, imprime que a categoria não é 'Fast Food'
    print('A categoria não é Fast Food.')



# Bloco 8: Ativar o restaurante
# Define o estado de 'ativo' do 'restaurante_pizza' para True
restaurante_pizza.ativo = True



# Bloco 9: Imprimir os atributos 'nome' e 'categoria' do 'restaurante_praca'
# Imprime os atributos 'nome' e 'categoria' do restaurante 'restaurante_praca'
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
