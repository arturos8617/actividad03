def square_area(side):
    return int(side)*4


def triangle_area(base, altura):
    return (int(base) * int(altura))/2


def circle_area(radio):
    return 3.1416 * (float(radio) * float(radio))


mainInput = '1'
while(mainInput != '0'):
    mainInput = input(
        '1.-Calcular area del cuadrado\n2.-Calcular area del triangulo\n3.-Calcular area del circulo\n0.-Salir')
    if(mainInput == '1'):
        print(square_area(input('Ingresa la medida del lado: ')))
    elif(mainInput == '2'):
        print(triangle_area(input('Ingresa la medida de la base: '),
              input('Ingresa la medida de la altura: ')))
    elif(mainInput == '3'):
        print(circle_area(input('Ingresa la medida del radio: ')))
