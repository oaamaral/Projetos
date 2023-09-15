# LISTAS (ESTUDANTES)
estudantes = []

while True: 
    # Menu principal
    print("Menu de operações:")
    print("1 - Estudantes")
    print("2 - Professores")
    print("3 - Disciplinas")
    print("4 - Turmas")
    print("5 - Matriculas")
    print("0 - Sair")

    # Opção do usuario
    opcao = input(" Digite sua escolha: ")

    if opcao == "1" or opcao == "2" or opcao == "3" \
            or opcao == "4" or opcao == "5":
        while True:
            print(f" Você acessou a opção {opcao} ")

            # Menu secundario
            print(f" Escolha sua opção")
            print("1 - Criar")
            print("2 - listar")
            print("3 - Atualizar")
            print("4 - Excluir")
            print("5 - Sair")

            # Opção do menu secundario
            opcao_secundaria = input("Digite uma opção valida: ")
            print(f"Opção secundaria {opcao_secundaria}")

            if "3" or opcao_secundaria == "4":
                print(f"Opção Secundaria VALIDA: {opcao_secundaria}")

            if opcao_secundaria == "1":
                nome = input("Adicionar estudante: ")
                estudantes.append (nome)
                continue

            if opcao_secundaria == "2":
                print(" Lista Dos estudantes ")
                for i in estudantes:
                    print("-", i)

            elif opcao_secundaria == "5":
                break
            else:
                print("AÇÃO INVALIDA!")
    elif opcao == "0":
        print("Até Logo")
        break
    else:
        print("Opção invalida!")
