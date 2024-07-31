import os

nomes_restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def main():
    limpar_sistema()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Mudar o estado do Restaurante')
    print('4. Sair')

def escolher_opcao():
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
    limpar_sistema()
    print('Você escolheu a opção: Cadastrar Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante =  {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    nomes_restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    limpar_sistema()
    print('Você escolheu a opção: Listar Restaurante')
    for restaurante in nomes_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu()

def mudar_estado_do_restaurante():
    limpar_sistema()
    print('Você escolheu a opção: Mudar o estado do Restaurante')
    for restaurante in nomes_restaurantes:
        nome_restaurante = restaurante['nome']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        numero_restaurante = nomes_restaurantes.index(restaurante)
        print(f'{numero_restaurante+1} - {nome_restaurante} | {ativo}')
    numero_do_restaurante = int(input('Digite o numero do restaurante que deseja mudar o estado: '))
    estado_restaurante = False
    for restaurante in nomes_restaurantes:
        if (nomes_restaurantes.index(restaurante)+1) == numero_do_restaurante:
            estado_restaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante['nome']} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {restaurante['nome']} foi desativado com sucesso'
            print(mensagem)
    if not estado_restaurante:
        print('Restaurante não encontrado')
    voltar_ao_menu()

def finalizar_app():
    limpar_sistema()
    print('O programa esta encerrando, Bye bye')

def limpar_sistema():
    os.system('cls')

def opcao_invalida():
    print('Opção Inválida\n')
    voltar_ao_menu()

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

if __name__ == '__main__':
    main()