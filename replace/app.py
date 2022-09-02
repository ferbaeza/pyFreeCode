from dataclasses import replace


def replace_function():
    str="""Hola Mundo
    Este es un mensaje de prueba

    {
        "name":"Fernando",
        "surname":"Baeza",
        "email":"fbaezahurtado@gmail.com",
    }
    """

    print(str)
    word_to_replace = input('Seleccione la palabra a modificar: ')
    word_replacement = input('Seleccione la nueva palabra: ')
    print(str.replace(word_to_replace, word_replacement))


if __name__=='__main__':
    replace_function()