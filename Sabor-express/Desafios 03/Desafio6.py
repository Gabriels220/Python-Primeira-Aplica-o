def main():
    lista_de_numeros = [20, 30, 40, 50]
    soma = 0
    try:
        for i in lista_de_numeros:
            soma += i  # Acumula os valores na variável "soma"

        print(f'A soma de {lista_de_numeros} é igual a {soma}')

    except TypeError:
        print('Um elemento na lista não é um número.')

if __name__ == '__main__':
    main()