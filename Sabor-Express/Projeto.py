import os

print("""Sabor-Express
      """)

print('1. Cadastrar-Restaurantes')
print('2. Listar-Restaurantes')
print('3. Ativar-Restaurante')
print('4. Sair')

opcao_escolhida =int(input('\nEscolha uma opção: '))
#opcao_escolhida = int(opcao_escolhida)

def finalizar_app():
    os.system('cls')
    #os.system('clear') no mac
    print('Encerrando o app...\n')





if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()