# bibliotecas
import os 

# criar uma lista global
restaurantes = ['Pizza','Art Doce','Vicky','Millenium']

# funcao que lista o nome do programa
def exibir_nome_do_programa():
    print(""" 
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█

""")

# MENU
def exibir_funcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# definir funcao para finalizar o programa
def finalizar_app():
    exibir_subtitulos('Finalizando o aplicativo...')

    
def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu.')
    main()

# para exibir o titulo e limpar a tela
def exibir_subtitulos(texto):
    os.system('cls')
    print(texto)
    print()
    
# se o utilizador digitar uma opcao invalida
def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_menu_principal()
    
    # cadastrar restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome = input('\nDigite o nome do restaurante a cadastrar: ')
    restaurantes.append(nome)
    print(f'O restaurante: {nome} foi cadastrado com sucesso.\n')
    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulos('Listar restaurantes')
    # estrutura de repeticao para exibir os restaurantes na tela
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_menu_principal()
    
    # funcao para esoclher opcoes
def escolher_opcao():
    # usando try except 
    try:
        # input do usuario
        opcao_escolhida = int(input('Escolha uma opcao: '))
        # verificar as opcoes
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida ==2:
            listar_restaurantes()
        elif opcao_escolhida ==3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
    
# funcao main que chama as funcoes existentes no codigo
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_funcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
    