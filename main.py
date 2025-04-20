from menus import *
from acesso import *
from cadastro_pousada import *
from buscar_pousada import *
from Pausa import *
from reservas import *

while True:
    try:
        menu_principal()
        opc = input(">> ")
        if opc == '1':
            resultado = login_user()
            if resultado == True:
                while True:
                    menu_secundario()
                    opc2 = input(">> ")
                    if opc2 == '1':
                        os.system('cls')
                        cad_pousada()
                    elif opc2 == '2':
                        bus_pousada()
                    elif opc2 == '3':
                        os.system('cls')
                        exibir_pousadas()
                    elif opc2 == '4':
                        break
                    else:
                        os.system('cls')
                        print("Opção inválida")
            else:
                pause()
        elif opc == '2':
            cadastrar_usuario()
        elif opc == '3':
            print("Volte Sempre.")
            break
        else:
            print("Escolha uma opção válida.\n\n")
    except ValueError:
        print("Digite apenas números válidos. \n\n")