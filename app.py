# bibliotecas
import os 

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
    os.system('cls')
    # os.system('clear') // no mac
    print('Finalizando o app \n')
    
# input do usuario
opcao_escolhida = int(input('Escolha uma opcao: '))
# outra forma de converter a string em inteiro
# opcao_escolhida = int(opcao_escolhida)
# print('voce escolheu a opcao', opcao_escolhida)
# outra forma de passar a string
# print(f'voce escolheu a opcao {opcao_escolhida}')


    # funcao para esoclher opcoes
def escolher_opcao():
    # verificar as opcoes
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida ==2:
        print('Listar Restaurante')
    elif opcao_escolhida ==3:
        print('Ativar Restaurante')
    else:
        finalizar_app()
    
    
# funcao main que chama as funcoes existentes no codigo
def main():
    exibir_nome_do_programa()
    exibir_funcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
    