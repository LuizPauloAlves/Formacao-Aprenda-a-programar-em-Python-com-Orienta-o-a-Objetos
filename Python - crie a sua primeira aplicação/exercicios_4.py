# Bloco 1: Criar e exibir um dicionário com informações de uma pessoa
# Cria um dicionário chamado 'pessoa' com três pares de chave-valor: nome, idade e cidade
pessoa = {'nome': 'João', 'idade': 20, 'cidade': 'São Paulo'}
# Imprime o dicionário 'pessoa' completo
print(pessoa)


# Bloco 2: Modificar o dicionário 'pessoa' e manipular suas chaves
# Atualiza o valor da chave 'idade' para 21 no dicionário 'pessoa'
pessoa['idade'] = 21
# Adiciona uma nova chave 'profissao' com o valor 'estudante' ao dicionário 'pessoa'
pessoa['profissao'] = 'estudante'
# Imprime o dicionário 'pessoa' após as modificações
print(pessoa)
# Remove a chave 'profissao' do dicionário 'pessoa'
pessoa.pop('profissao')
# Imprime o dicionário 'pessoa' após a remoção da chave 'profissao'
print(pessoa)


# Bloco 3: Criar um dicionário que mapeia números aos seus quadrados
# Inicializa um dicionário vazio chamado 'numeros_quadrados'
numeros_quadrados = {}
# Usa um loop 'for' para iterar sobre os números de 1 a 5 (inclusive)
for i in range(1, 6):
    # Adiciona uma entrada no dicionário onde a chave é o número 'i' e o valor é o quadrado de 'i'
    numeros_quadrados[i] = i * i
# Imprime o dicionário 'numeros_quadrados' que contém os números de 1 a 5 e seus quadrados
print(numeros_quadrados)


# Bloco 4: Buscar o valor de uma chave específica em um dicionário
# Solicita ao usuário para digitar uma chave (um número inteiro)
chave_especifica = int(input('Digite a chave para encontrar o seu quadrado: '))
# Verifica se a chave fornecida pelo usuário existe no dicionário 'numeros_quadrados'
if numeros_quadrados.get(chave_especifica) is not None:
    # Se a chave existe, imprime o valor associado a essa chave
    print(numeros_quadrados[chave_especifica])
else:
    # Se a chave não existe, imprime uma mensagem de erro
    print('Eita Bixo! A chave não foi encontrada.')


# Bloco 5: Contar a frequência de cada palavra em uma frase usando um dicionário
# Define uma string 'frase' que será analisada
frase = 'Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário'
# Inicializa um dicionário vazio chamado 'palavras' para armazenar a frequência das palavras
palavras = {}
# Inicializa uma string vazia chamada 'palavra' para construir palavras individualmente
palavra = ''
# Define uma função para atualizar a contagem de uma palavra no dicionário 'palavras'
def preencher_dicionario(palavra, palavras):
    # Se a palavra já está no dicionário, incrementa sua contagem
    if palavra in palavras:
        palavras[palavra] += 1
    else:
        # Se a palavra não está no dicionário, adiciona-a com uma contagem inicial de 1
        palavras[palavra] = 1
# Itera sobre cada caractere da 'frase'
for i in frase:
    # Verifica se o caractere atual é um espaço, indicando o fim de uma palavra
    if i == ' ':
        # Se for o fim de uma palavra, chama a função para atualizar o dicionário com a palavra completa
        preencher_dicionario(palavra, palavras)
        # Reseta a variável 'palavra' para iniciar a próxima palavra
        palavra = ''
    else:
        # Se não for um espaço, adiciona o caractere à palavra em construção
        palavra += i
# Após o loop, verifica se há uma palavra restante para adicionar ao dicionário
if palavra:
    preencher_dicionario(palavra, palavras)
# Imprime o dicionário 'palavras' que contém a frequência de cada palavra na frase
print(palavras)