def login():
    nome = 'gabriel.mendes'
    senha = 'frango123'

    nome_usuario = input('Digite o nome: ')
    senha_usuario = input('Digite a senha: ')

    if nome_usuario == nome and senha_usuario == senha:
        print('Entrou!')
    else: print('O nome ou a senha estão incorretos')

def main():
    login()

if __name__ == '__main__':
    main()