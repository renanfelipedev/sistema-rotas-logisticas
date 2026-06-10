def cadastrar_motoristas():
    print("Digite as informações do motorista")
    nome = input("Digite o nome do motorista: ")
    idade = int(input("Digite a idade do motorista: "))
    cpf = int(input("Digite o cpf do motorista"))
    cnh = int(input("Digite a numeração da CNH do motorista: "))
    with open("lista_de_motoristas.txt", "w", encoding="utf-8") as cadastro_de_motoristas:
        cadastro_de_motoristas.write(f"Nome do motorista: {nome} | Idade: {idade} | cpf: {cpf} | cnh: {cnh}")

def listar_motoristas():
    with open("lista_de_motoristas.txt", "r", encoding="utf-8") as cadastro_de_motoristas:
        for linha in cadastro_de_motoristas:
            print(linha)
        
