import funcoes 
import os
import csv
def menu():
    

    while True:
        print("---------------------------------")
        print("  SISTEMA DE ROTAS DE LOGISTICA  ")
        print("---------------------------------")
        print("\n")
        print("1 - Cadastarar motoristas")
        print("2 - Listar motoristas")
        print("3 - Registrar viagens")
        print("4 - Listar viagens")
        print("5 - total gasto com combustível e quilômetros rodados")
        print("0 - Sair")

with open("motoristas.csv", "w", newline="", encoding="utf-8") as arquivo:
    motorista = csv.writer(arquivo)

    
    motorista.writerow(["Nome","Idade", "CPF", "CNH"])

with open("rotas_viagens.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)


menu()

opcao = int(input("Escolha uma opção: "))
match opcao:
    case 1:
        funcoes.cadastrar_motoristas()
    case 2:
        funcoes.listar_motoristas()
    case 3:
        funcoes.registar_viagem()



