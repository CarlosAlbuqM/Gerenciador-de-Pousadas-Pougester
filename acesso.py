from Pausa import *

def carregar_usuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "r") as file:
            for linha in file:
                nome, senha = linha.strip().split(",")
                usuarios.append([nome, senha])
    except FileNotFoundError:
        pass
    return usuarios

usuarios = carregar_usuarios()

def salvar_usuario(nome, senha):
    with open("usuarios.txt", "a") as file:
        file.write(f"{nome},{senha}\n")

def login_user():

    print(" >> Login << ")
    nome_usuario = input("Nome de usuário: \n >> ").strip()

    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            senha = input("Digite sua senha: \n >> ").strip()
            if usuario[1] == senha:
                print(f" Bem-vindo, {nome_usuario}! \n")
                return True
            else: 
                print("Senha incorreta. Tente novamente")
                return False
    print("Usuário não cadastrado.")
    return False

def cadastrar_usuario():

    print (" >> Cadastrar <<")
    nome_usuario = input("Digite o nome do usuário \n >> ")
    senha = input("Digite sua senha \n >>")

    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            print("Nome de usuário já cadastrado. Tente outro. \n")
            return False
    usuarios.append([nome_usuario, senha])
    salvar_usuario(nome_usuario, senha)
    print(f"Usuário {nome_usuario}, foi cadastrado com sucesso.")
    return 

