# Bloco 1: Definir e inicializar listas
# Define uma lista de números de 1 a 10
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Define uma lista de nomes em formato textual, representando números
lista_nomes = ['zero', 'um', 'dois', 'tres']
# Define uma lista de anos representativos
lista_anos = [1993, 2024]


# Bloco 2: Iterar sobre listas e imprimir os elementos
# Itera sobre cada número em 'lista_numeros' e o imprime
for numero in lista_numeros:
    print(f'{numero}')
# Itera sobre cada nome em 'lista_nomes' e o imprime
for nome in lista_nomes:
    print(f'{nome}')
# Itera sobre cada ano em 'lista_anos' e o imprime
for anos in lista_anos:
    print(f'{anos}')


# Outro modo de fazer Bloco 2: Utilizando uma função para ler e imprimir listas
# Define uma função que recebe uma lista e imprime cada elemento da lista
def ler_lista(lista):
    for variavel in lista:
        print(f'{variavel}')
# Itera sobre uma lista de listas (lista_numeros, lista_nomes, lista_anos)
# e passa cada lista para a função 'ler_lista' para ser processada
for i in [lista_numeros, lista_nomes, lista_anos]:
    ler_lista(i)


# Bloco 3: Calcular a soma dos números ímpares em uma lista
# Inicializa uma variável 'total' com zero para armazenar a soma dos números ímpares
total = 0
# Itera sobre cada número na lista 'lista_numeros'
for soma in lista_numeros:
    # Verifica se o número é ímpar usando o operador de módulo (%)
    # Um número é ímpar se o resto da divisão por 2 for diferente de zero (soma % 2 != 0)
    if soma % 2 != 0:
        # Se a condição for verdadeira, adiciona o número ao 'total'
        total += soma
# Imprime o valor total da soma dos números ímpares
print(total)


# Bloco 4: Imprimir números em ordem decrescente
# Itera sobre 'lista_numeros' em ordem reversa (do último ao primeiro) usando slicing
for decrescente in lista_numeros[::-1]:
    print(decrescente)


# Bloco 5: Exibir a tabuada de um número específico
# Solicita ao usuário um número para o qual deseja ver a tabuada
numero_tabuada = int(input('Qual tabuada deseja, informe o numero: '))
# Itera sobre cada número em 'lista_numeros' e imprime o resultado da multiplicação
# do número pelo 'numero_tabuada'
for valor in lista_numeros:
    print(f'{valor} * {numero_tabuada} = {valor * numero_tabuada}')


# Bloco 6: Coletar números de entrada do usuário e exibir a lista coletada
# Inicializa uma lista vazia para armazenar os números digitados pelo usuário
lista_de_input_de_numeros = []
# Inicia um loop infinito para coletar entradas do usuário
while True:
    try:
        # Solicita ao usuário para digitar um valor e tenta convertê-lo para inteiro
        valor = int(input('Digite um valor:'))
        # Adiciona o valor convertido à lista 'lista_de_input_de_numeros'
        lista_de_input_de_numeros.append(valor)
    except:
        # Interrompe o loop se ocorrer uma exceção (por exemplo, quando a entrada não é um número)
        break
# Itera sobre cada número na lista 'lista_de_input_de_numeros' e o imprime
for numero in lista_de_input_de_numeros:
    print(f'{numero}')


# Bloco 7: Calcular a média dos números coletados
# Inicializa uma variável 'soma' com zero para acumular os números
soma = 0
# Itera sobre cada número na lista 'lista_de_input_de_numeros' e acumula o valor em 'soma'
for numero in lista_de_input_de_numeros:
    soma += numero
try:
    # Tenta calcular a média dividindo a soma pelo número de elementos na lista
    media = soma / len(lista_de_input_de_numeros)
    # Imprime o valor da média
    print(media)
except:
    # Se ocorrer uma exceção (como divisão por zero), imprime uma mensagem de erro
    print('erro!')