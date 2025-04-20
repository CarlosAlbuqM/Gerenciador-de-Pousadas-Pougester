from Pausa import *
import os

def carregar_pousadas():
    pousadas = []
    try:
        with open("pousadas.txt", "r") as file:
            for linha in file:
                nome, diaria, cidade, endereco, quartos = linha.strip().split("|")
                pousadas.append({
                    "nome": nome,
                    "diaria": float(diaria),
                    "cidade": cidade,
                    "endereco": endereco,
                    "quartos_disp": int(quartos)
                })
    except FileNotFoundError:
        pass
    return pousadas

listaPousada = carregar_pousadas()

def salvar_pousada(pousada):
    with open("pousadas.txt", "a") as file:
        file.write(f"{pousada['nome']}|{pousada['diaria']}|{pousada['cidade']}|{pousada['endereco']}|{pousada['quartos_disp']}\n")
    return None


def cad_pousada():
    print (" >> Cadastrar Pousada <<")
    nome = input("Digite o nome da pousada que gostaria de cadastrar:  \n >> ")
    diaria = float(input("Digite o preço da diária:  \n >> R$"))
    cidade = str(input("Digite a cidade onde a pousada fica localizada: \n >> "))
    endereco = input("Digite o endereço da Pousada: \n >>")
    quartos_disp = int(input("Digite a quantidade de quartos que estão disponíveis:  \n >> "))

    pousada = {
        "nome": nome,
        "diaria": diaria,
        "cidade": cidade,
        "endereco": endereco,
        "quartos_disp": quartos_disp,
    }

    listaPousada.append(pousada)
    salvar_pousada(pousada)
    print(" >> Pousada cadastrada com sucesso <<")
    pause()
    os.system('cls')

def exibir_pousadas():
    print(" >> Lista de Pousadas Cadastradas <<\n")
    if not listaPousada:
        print("Nenhuma pousada cadastrada.")
    for pousada in listaPousada:
        print(f"Nome: {pousada['nome']}")
        print(f"Diária: R$ {pousada['diaria']:.2f}")
        print(f"Cidade: {pousada['cidade']}")
        print(f"Endereço: {pousada['endereco']}")
        print(f"Quartos disponíveis: {pousada['quartos_disp']}")
        print("-" * 30)