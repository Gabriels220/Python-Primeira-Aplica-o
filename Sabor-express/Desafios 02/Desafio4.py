
#primeiro_quadrante = coordenada_x_usuario and coordenada_y_usuario > 0
#segundo_quadrante = coordenada_x_usuario < 0 and coordenada_y_usuario > 0
#terceiro_quadrante = coordenada_x_usuario and coordenada_y_usuario < 0
#quarto_quadrante = coordenada_x_usuario > 0 and coordenada_y_usuario < 0

def plano_cartesiano():
    coordenada_x_usuario = float(input('Coordenada X: '))
    coordenada_y_usuario = float(input('Coordenada Y: '))

    if coordenada_x_usuario > 0 and coordenada_y_usuario > 0:
        print('Primeiro Quadrante')
    elif coordenada_x_usuario < 0 and coordenada_y_usuario > 0:
        print('Segundo Quadrante')
    elif coordenada_x_usuario < 0 and coordenada_y_usuario < 0:
        print('Terceiro Quadrante')
    elif coordenada_x_usuario > 0 and coordenada_y_usuario < 0:
        print('Quarto Quadrante')
    else:
        print('Eixo ou Origem')

def main():
    plano_cartesiano()

if __name__ == '__main__':
    main()