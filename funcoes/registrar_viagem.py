import os
import csv

def registar_viagem():
    print("Digite as informações da viagem")

    origem = input("Digite a origem da viagem: ")
    destino = input("Digite o destino da viagem: ")
    distancia = float(input("Digite a distância da viagem (km): "))
    consumo = float(input("Digite o consumo da viagem (L): "))
    motorista = input("Escreva o nome do motorista: ")

    arquivo = "rotas_viagens.csv"
    arquivo_existe = os.path.isfile(arquivo)

    with open(arquivo, "a", newline="", encoding="utf-8") as cadastro:
        campos = ["origem", "destino", "distancia", "consumo", "motorista"]

        writer = csv.DictWriter(
            cadastro,
            fieldnames=campos,
            delimiter=";"
        )

        if not arquivo_existe:
            writer.writeheader()

        writer.writerow({
            "origem": origem,
            "destino": destino,
            "distancia": f"{distancia:.1f} km",
            "consumo": f"{consumo:.1f} L",
            "motorista": motorista
        })

    print("Viagem cadastrada com sucesso!")



