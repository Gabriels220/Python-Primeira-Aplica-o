
def main():
    numero_da_tabuada = int(input('Digite o Número que deseja ver a sua tabuada: '))

    for i in range(1, 11):
        resultado = numero_da_tabuada * i
        print(f'{numero_da_tabuada} x {i} = {resultado}')


if __name__ == '__main__':
    main()