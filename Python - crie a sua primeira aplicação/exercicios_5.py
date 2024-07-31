import os

# Lista de restaurantes com seus nomes, categorias e status de atividade
nomes_restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                      {'nome': 'Pizza Superma', 'categoria': 'Pizza', 'ativo': True},
                      {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def main():
    """
    Função principal que inicia o aplicativo de gerenciamento de restaurantes.

    Esta função limpa o sistema, exibe o nome do programa, mostra as opções
    de menu e solicita ao usuário que escolha uma opção.

    input:
        None

    output:
        None
    """
    limpar_sistema()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def exibir_nome_do_programa():
    """
    Exibe o nome do programa na interface do usuário.

    input:
        None

    output:
        None
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    """
    Exibe as opções de menu disponíveis para o usuário.

    input:
        None

    output:
        None
    """
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Mudar o estado do Restaurante')
    print('4. Sair')

def escolher_opcao():
    """
    Solicita ao usuário que escolha uma opção do menu e executa a ação correspondente.

    input:
        None

    output:
        None
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            mudar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    """
    Solicita informações do usuário e cadastra um novo restaurante na lista.

    input:
        None

    output:
        None
    """
    limpar_sistema()
    print('Você escolheu a opção: Cadastrar Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    nomes_restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    """
    Exibe uma lista de todos os restaurantes cadastrados.

    input:
        None

    output:
        None
    """
    limpar_sistema()
    print('Você escolheu a opção: Listar Restaurantes')
    for restaurante in nomes_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu()

def mudar_estado_do_restaurante():
    """
    Solicita ao usuário que escolha um restaurante e altera seu estado de ativo para inativo ou vice-versa.

    input:
        None

    output:
        None
    """
    limpar_sistema()
    print('Você escolheu a opção: Mudar o estado do Restaurante')
    for restaurante in nomes_restaurantes:
        nome_restaurante = restaurante['nome']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        numero_restaurante = nomes_restaurantes.index(restaurante)
        print(f'{numero_restaurante + 1} - {nome_restaurante} | {ativo}')
    numero_do_restaurante = int(input('Digite o número do restaurante que deseja mudar o estado: '))
    estado_restaurante = False
    for restaurante in nomes_restaurantes:
        if (nomes_restaurantes.index(restaurante) + 1) == numero_do_restaurante:
            estado_restaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante["nome"]} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {restaurante["nome"]} foi desativado com sucesso'
            print(mensagem)
    if not estado_restaurante:
        print('Restaurante não encontrado')
    voltar_ao_menu()

def finalizar_app():
    """
    Encerra a execução do aplicativo de gerenciamento de restaurantes.

    input:
        None

    output:
        None
    """
    limpar_sistema()
    print('O programa está encerrando, Bye bye')

def limpar_sistema():
    """
    Limpa a tela do console.

    input:
        None

    output:
        None
    """
    os.system('cls')

def opcao_invalida():
    """
    Informa ao usuário que a opção selecionada é inválida.

    input:
        None

    output:
        None
    """
    print('Opção Inválida\n')
    voltar_ao_menu()

def voltar_ao_menu():
    """
    Solicita ao usuário que pressione uma tecla para voltar ao menu principal.

    input:
        None

    output:
        None
    """
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

if __name__ == '__main__':
    main()
