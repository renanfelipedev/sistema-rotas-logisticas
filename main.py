import motoristas
import csv
print("---------------------------------")
print("  SISTEMA DE ROTAS DE LOGISTICA  ")
print("---------------------------------")
print("\n")
print("1 - Cadastarar motoristas")
print("2 - Listar motoristas")
print("3 - Registro de viagens")
print("4 - total gasto com combustível e quilômetros rodados ")
print("5 - Sair")

with open("motoristas.csv", "w", newline="", encoding="utf-8") as arquivo:
    motorista = csv.writer(arquivo)

    
    motorista.writerow(["Nome","Idade", "CPF", "CNH"])

with open("rotas_viagens.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)


 

opcao = int(input("Escolha uma opção: "))
match opcao:
    case 1:
        motoristas.cadastrar_motoristas()
    case 2:
        motoristas.listar_motoristas()



