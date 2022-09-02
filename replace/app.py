def main():
    str = """\nHello World

    My name is Fernando
    Welcome to Python

    """
    print(str)
    str_to_replace = input('Introduce la palabra que desea cambiar: ')
    str_replacement = input('Introduce la nueva palabra: ')
    print('\n')
    print(str.replace(str_to_replace, str_replacement))
if __name__=='__main__':
    main()