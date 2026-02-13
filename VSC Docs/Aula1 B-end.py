Usuarios = {}
while True:
    print("1- Cadastrar:")
    print("2- Login")
    print("3- Sair")
    opção = input("Escolha:")

    if opção == "1":
        login = input("Login:").strip()
        if login in Usuarios or login == "":
            print("login inválido ou já existente")
            continue
        senha = input("Senha: ").strip()
        Usuarios[login] = senha
        print("Usuário Cadastrado!")

    elif opção == "2":
        login = input("Login:").strip()
        senha = input("Senha:").strip()
        if login in Usuarios and Usuarios[login] == senha:
            print("Login Realizado")
        else:
            print("Login Incorreto")
    elif opção == "3":
        break