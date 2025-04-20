from cadastro_pousada import *
from buscar_pousada import *
from Pausa import *
import os


def alugar_quarto():
    print(" >> Reserva de Quarto << ")
    nome_pousada = input("Informe o nome da Pousada na qual gostaria de se hospedar. \n >> ")
    encontrou = False

    for pousada in listaPousada:
        if pousada["nome"] == nome_pousada:
            encontrou = True
            print(f"Cidade: {pousada['cidade']}\n Diária: R${pousada['diaria']}\nEndereço: {pousada['endereco']}\n Quartos disponíveis: {pousada['quartos_disp']}")
            quantidade_quartos = int(input("Digite o número de reservas que gostaria de fazer. \n >> "))
            if quantidade_quartos > pousada["quartos_disp"]:
                print("Quantidades de quartos indisponível")
                return
            else:
                quantidade_dias = int(input("Digite o número de dias que ficará hospedado. \n >> "))
                valor_final = pousada["diaria"] * quantidade_quartos * quantidade_dias
                print(f"O valor da reserva ficou R${valor_final:.2f}. \nReserva realizada com sucesso.\n\n")
                pousada["quartos_disp"] -= quantidade_quartos
                break
    if encontrou == False:
        print("Pousada sem cadastro no sistema.")
        return
    pause()
    os.system('cls')