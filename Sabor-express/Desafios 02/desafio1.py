def verificar_numero():
    numero = int(input('Digite o número desejado: '))
    if numero < 0:
        print('Número inválido, digite outro número')
        main()
    elif numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')

def main():
    verificar_numero()  

if __name__ == '__main__':
    main()     

