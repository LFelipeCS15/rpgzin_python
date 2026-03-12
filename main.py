def escolha_classe():
    print("Escolha sua classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Arqueiro")
    print("4. Ladino")

    classe = input("Qual sua classe? (1/2/3/4): ")

    
    if classe == "1":
        classe = "Guerreiro"
        print(f"\n{nome}, você escolheu o caminho do Guerreiro!")
        print("")
        print(f"Iniciando a jornada de {nome} o Guerreiro...")
        print("")
        return classe
    elif classe == "2":
        classe = "Mago"
        print(f"\n{nome}, você escolheu o caminho do Mago!")
        print("")
        print(f"Iniciando a jornada de {nome} o Mago...")
        print("")
        return classe
    elif classe == "3":
        classe = "Arqueiro"
        print(f"\n{nome}, você escolheu o caminho do Arqueiro!")
        print("")
        print(f"Iniciando a jornada de {nome} o Arqueiro...")
        print("")
        return classe
    elif classe == "4":
        classe = "Ladino"
        print(f"\n{nome}, você escolheu o caminho do Ladino!")
        print("")
        print(f"Iniciando a jornada de {nome} o Ladino...")
        print("")
        return classe
    else:
        print("Classe inválida. Tente novamente.")
        escolha_classe()

def jornada():
    print("Você a muito tempo sonha em se tornar um aventuiro.")
    print("Se aventurar por terras desconhecidas, enfrentar monstros e descobrir tesouros.")
    print(f"Por isso você treinou para se tornar um {classe} e finalmente ir em sua jornada.")
    print("Você se encontra nos portões do Reino de Vale, conhecido por ser o Reino dos Aventureiros.")
    print("Um reino cheio de pessoas de diversas raças, vindas de diversos lugares.")
    print("Cheio de guildas e comercios, onde você pode encontrar tudo o que precisa para sua jornada.")
    print("")
    print("Você entra pelos portões olhando em volta, vendo a movimentação das pessoas, as lojas, as guildas, os bares e as tavernas.")
    print("Você se sente animado e pronto para começar sua aventura, mas antes de sair para explorar o reino, você decide ir até a taverna \nmais próxima para descansar e se preparar para o que está por vir.")

if __name__ == "__main__":
    nome = input("Digite seu nome, aventureiro: ")
    classe = escolha_classe()
    jornada()