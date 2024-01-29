import os

restaurantes = [{'nome':'Sal e Brasa', 'categoria':'churrascaria', 'ativo':True},
                {'nome':'Oliva', 'categoria':'pizzaria', 'ativo':False},
                {'nome':'Pezão', 'categoria':'bar', 'ativo':True}]

def exibir_nome_do_programa():
    '''Essa função exibe o nome'''
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opcoes():
    '''Essa função exibe as opções ao usuário'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar ou Desativar Restaurante')
    print('4. Finalizar Restaurante\n')


def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Essa função volta ao menu principal'''
    input('Digite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa função é utilizada como opção invalida para o else e o try except nos operadores ternários'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função exibe o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsávl por cadastrar um novo restaurante
    
    inputs: nome_novo
            categoria

    outputs: Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_novo = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do Restaurante {nome_novo}: ')
    dados_do_restaurante = {'nome': nome_novo, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_novo} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista todos os restaurantes cadastrados'''
    exibir_subtitulo('Listando Restaurantes')
    
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_novo = restaurante['nome']
        categorias = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_novo.ljust(20)} | {categorias.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Essa função ativa ou desativa o restaurante'''
    exibir_subtitulo('Alternando estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa função é responsável por apresentar as alternativas das funções ao usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()