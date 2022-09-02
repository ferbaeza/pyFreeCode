def suma(a,b):
    answer = a + b
    print('\nSuma: '+str(a)+'+'+str(b)+'= '+str(answer))

def resta(a,b):
    answer = a - b
    print('\nResta: '+str(a)+'-'+str(b)+'= '+str(answer))

def mult(a,b):
    answer = a * b
    print('\nMultiplicacion: '+str(a)+'*'+str(b)+'= '+str(answer))

def div(a,b):
    answer = a / b
    print('\nDivision: '+str(a)+'/'+str(b)+'= '+str(answer))

def main():
    op=''
    while op != '0':
        print("""
        1_Suma
        2_Resta
        3_Multiplicacion
        4_Division

        0_Salir
        """)
        op = input('Elige que operacion deseas realizar:  ')

        if op =='1':
            print('Suma')
            a= int(input('Introduzca el numero 1:  '))
            b= int(input('Introduzca el numero 2:  '))
            suma(a,b)
        elif op =='2':
            print('Resta')
            a= int(input('Introduzca el numero 1:  '))
            b= int(input('Introduzca el numero 2:  '))
            resta(a,b)
        elif op =='3':
            print('Multiplicacion')
            a= int(input('Introduzca el numero 1:  '))
            b= int(input('Introduzca el numero 2:  '))
            mult(a,b)
        elif op =='4':
            print('Division')
            a= int(input('Introduzca el numero 1:  '))
            b= int(input('Introduzca el numero 2:  '))
            div(a,b)



if __name__=='__main__':
    main()