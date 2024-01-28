#Desafio 6 


def main():
    lista_de_numeros = [2, 3, 4, 50]
    soma = 0
    try:
        for i in lista_de_numeros:
            soma += i  # Acumula os valores na variável "soma"

        print(f'A soma de {lista_de_numeros} é igual a {soma}')

    except TypeError:
        print('Um elemento na lista não é um número.')

if __name__ == '__main__':
    main()