#Desafio 3


def main():
    soma_impares = 0
    for i in range(1,11):
        if i % 2 != 0:
            soma_impares = soma_impares + i

    print(f'A soma dos numeros impares entre 1 e 10 são: {soma_impares}')
            
    

if __name__ == '__main__':
    main()