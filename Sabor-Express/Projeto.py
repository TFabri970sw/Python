import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japones', 'ativo':False},
                {'nome': 'The big pizza', 'categoria':'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_apcoes():
        print('1. Cadastrar-Restaurantes')
        print('2. Listar-Restaurantes')
        print('3. Ativar-Restaurante')
        print('4. Sair')

def finalizar_app():
    exibir_subtitulo('Encerrando o app...')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para volta ao menu principal ')
    main()

def opcao_invalida():
    print('Opcão inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo (texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_um_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes\n')
    #para cada restaurante na lista  restaurantes:
    #nome
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu_principal()

    
def escolher_opcaoes():
    try:
        opcao_escolhida =int(input('\nEscolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_um_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_apcoes()
    escolher_opcaoes()

if __name__ ==  '__main__':
    main()