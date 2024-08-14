# Direitos de Manuel Figueiredo
import os 

# criar uma lista global
restaurantes = [{'nome':'Art Doce', 'categoria':'Huilana', 'ativo':False},
                {'nome':'Millenium','categoria':'africana','ativo':False},
                {'nome':'Doces da Vicky','categoria':'Doces e Salgados','ativo':True}
                ]

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
    print('3. Alternar estado do restaurante')
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
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
    
# se o utilizador digitar uma opcao invalida
def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_menu_principal()
    
    # cadastrar restaurante
def cadastrar_novo_restaurante():
    '''Funcao que cadastra novo restaurante'''
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('\nDigite o nome do restaurante a cadastrar: ')
    categoria = input(f' Digite a categoria do restaurante {nome_do_restaurante}: ')
    # estaado = input(f'Diga o estado do produto {ativo}: ')
    dados = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    # salvar os dados na lista
    restaurantes.append(dados)
    print(f'O restaurante: {nome} foi cadastrado com sucesso.\n')
    voltar_menu_principal()
    
def listar_restaurantes():
    '''Funcao para listar os restaurantes'''
    exibir_subtitulos('Listar restaurantes')
    # estrutura de repeticao para exibir os restaurantes na tela
    # para definir espacamento entre as palavras de 20
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desactivado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()
    
# funcao para alternar
def alternar_estado_restaurante():
    '''Funcao para alternar o estado do restaurante'''
    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi activado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('\nO restaurante nao foi encontrado.')
    
    
    voltar_menu_principal()
    
    
    # funcao para esoclher opcoes
def escolher_opcao():
    '''Funcao para escholher as opcoes'''
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
            alternar_estado_restaurante()
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
    