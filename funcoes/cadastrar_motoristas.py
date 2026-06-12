import csv
import os

def cadastrar_motoristas():
    print("Digite as informações do motorista")
    nome = input("Digite o nome do motorista: ")
    idade = int(input("Digite a idade do motorista: "))
    cpf = input("Digite o CPF do motorista: ")
    cnh = input("Digite a numeração da CNH do motorista: ")

    arquivo = "lista_de_motoristas.csv"
    arquivo_existe = os.path.isfile(arquivo)

    with open(arquivo, "a", newline="", encoding="utf-8") as cadastro:
        campos = ["Nome", "Idade", "CPF", "CNH"]
        writer = csv.DictWriter(cadastro, fieldnames=campos)

        if not arquivo_existe:
            writer.writeheader()

        writer.writerow({
            "Nome": nome,
            "Idade": idade,
            "CPF": cpf,
            "CNH": cnh
        })

    print(f"Motorista '{nome}' cadastrado com sucesso!")