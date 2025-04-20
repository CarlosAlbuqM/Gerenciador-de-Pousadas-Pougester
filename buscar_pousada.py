from cadastro_pousada import listaPousada
from Pausa import *
from reservas import *


def bus_pousada():
    while True:
        print(" >> Buscar Pousada << ")
        cidade = str(input("Digite a cidade Desejada. \n >> "))
        encontrou_pousada = False
        for pousada in listaPousada:
            if pousada["cidade"].lower() == cidade.lower():
                print(f"Nome: {pousada['nome']}\nPreço: R$ {pousada['diaria']}\nCidade: {pousada['cidade']}\nEndereço: {pousada['endereco']}\nQuartos Disponíveis: {pousada['quartos_disp']}\n\n")
                encontrou_pousada = True
        if encontrou_pousada == True:
            escolha = str(input("Deseja fazer uma reserva agora ? (s/n) \n >> ")).lower()
            if escolha == 's':
                alugar_quarto()
            elif escolha == 'n':
                print("Retornar ao menu...")
                pause()
                break
            else:
                print("Entrada inválida. Digite apenas 's' ou 'n'")
        if encontrou_pousada == False:
                    print("Não existe nenhuma pousada disponível nesta cidade. Tente novamente. \n")
        break