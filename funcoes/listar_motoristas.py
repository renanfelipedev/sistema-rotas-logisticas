import os
import csv
def listar_motoristas():
    import csv
    with open("lista_de_motoristas.csv", "r", encoding="utf-8") as cadastro:
        reader = csv.DictReader(cadastro)
        for motorista in reader:
            print(f"Nome: {motorista['Nome']} | Idade: {motorista['Idade']} | CPF: {motorista['CPF']} | CNH: {motorista['CNH']}")


