# Bloco 1: Verificar se um número é par ou ímpar
# Solicita ao usuário para digitar um valor e o converte para inteiro
numero = int(input('Digite um valor:'))
# Verifica se o número é par usando o operador de módulo (%)
# Se o resto da divisão de 'numero' por 2 for igual a 0, é par
if numero % 2 == 0:
    # Se a condição for verdadeira, imprime que o número é par
    print(f'{numero} é Par')
else:
    # Caso contrário, imprime que o número é ímpar
    print(f'{numero} é Impar')



# Bloco 2: Determinar a fase da vida com base na idade
# Solicita ao usuário para inserir a idade e converte para inteiro
idade = int(input('Qual a sua idade:'))
# Verifica se a idade é maior que 18 anos
if idade > 18:
    # Se a condição for verdadeira, o usuário é considerado um adulto
    print('Você é um Adulto')
# Verifica se a idade está entre 13 e 18 anos (inclusive)
elif 18 >= idade > 12:
    # Se a condição for verdadeira, o usuário é considerado um adolescente
    print('Você é um Adolescente')
# Verifica se a idade está entre 0 e 12 anos (inclusive)
elif 12 >= idade >= 0:
    # Se a condição for verdadeira, o usuário é considerado uma criança
    print('Você é um Criança')
else:
    # Se nenhuma das condições anteriores for verdadeira, considera-se um valor inválido
    print('Você é um Alien')



# Bloco 3: Autenticação de login e senha
# Define as credenciais válidas para login e senha
login = 'Login'
senha = 'senha'
# Solicita ao usuário para digitar o login
input_login = input('Digite o Login: ')
# Solicita ao usuário para digitar a senha
input_senha = input('Digite a Senha: ')
# Verifica se tanto o login quanto a senha inseridos pelo usuário são corretos
if login == input_login and senha == input_senha:
    # Se ambas as credenciais estiverem corretas, imprime que a entrada é válida
    print('Entrada Valida!')
else:
    # Caso contrário, imprime uma mensagem de falha de autenticação
    print('Blitz, documentos! Ué, só temos instrumentos!')



# Bloco 4: Determinar o quadrante de um ponto no plano cartesiano
# Solicita ao usuário para inserir as coordenadas X e Y separadas por espaço
coordenadas = input('Digite as coordenadas (X e Y separadas por espaço): ')
# Separa a entrada em duas partes e converte-as para inteiros
coordenadas_X, coordenadas_Y = map(int, coordenadas.split())
# Verifica se o ponto está no primeiro quadrante (X > 0 e Y > 0)
if coordenadas_X > 0 and coordenadas_Y > 0:
    print('Primeiro Quadrante')
# Verifica se o ponto está no segundo quadrante (X < 0 e Y > 0)
elif coordenadas_X < 0 and coordenadas_Y > 0:
    print('Segundo Quadrante')
# Verifica se o ponto está no terceiro quadrante (X < 0 e Y < 0)
elif coordenadas_X < 0 and coordenadas_Y < 0:
    print('Terceiro Quadrante')
# Verifica se o ponto está no quarto quadrante (X > 0 e Y < 0)
elif coordenadas_X > 0 and coordenadas_Y < 0:
    print('Quarto Quadrante')
else:
    # Se o ponto não estiver em nenhum dos quadrantes, ele está na origem ou em algum dos eixos
    print('Origem ou Eixo X ou Eixo Y')