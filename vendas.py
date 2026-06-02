import os
opcao = 0

while opcao != 3:
    print("-------------- MENU DE CADASTRO --------------")
    print("1 - Cadastrar dados")
    print("2 - Listar usuários")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
 
    if (opcao == 1):
        nome = input("Insira seu nome: ")
        email = input("Insira seu email: ")
        telefone = input("Insira seu telefone: ")

        arquivo = open("cad_pessoas.txt", "r")
        arquivo.write(f"{nome}, {telefone}, {email}")
        arquivo.close()
        

        print("Seus dados foram cadastrados com sucesso!")
        input()
        os.system("cls")
        
   
    if opcao == 2:
        print("----------------Lista---------------")

        for linha in arquivo:
            nome, telefone, email = linha.strip().split(",")
            print(f"Nome da pessoa: {nome}")
            print(f"Nome da telefone: {telefone}")
            print(f"Nome da email: {email}")
        arquivo.close()


        input()
        os.system("cls")

