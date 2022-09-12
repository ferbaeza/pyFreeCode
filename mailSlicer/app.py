from distutils import extension


def main():
    print('Hello and Welcome to email_Slicer_App')
    print('')

    email_input= input('Introduce tu email: \n')
    (username, domain)= email_input.split('@')
    (domain, extension)= domain.split('.')
    print('Username: '+username)
    print('Dominio: '+domain)
    print('Extension: '+extension)







if __name__=='__main__':
    main()