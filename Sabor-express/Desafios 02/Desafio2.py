def verificar_idade():
    idade = int(input('Digite a sua idade: '))
    crianca = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    adolescente = [13,14,15,16,17]

    if idade in crianca:
        print(f'{idade} anos corresponde a categoria "Criança".')
    elif idade in adolescente:
        print(f'{idade} anos corresponde a categoria "Adolescente".') 
    else:
        print(f'{idade} anos corresponde a categoria "Adulto".')

def main():
    verificar_idade()

if __name__ == '__main__':
    main()