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
        print("Iniciando a jornada do Guerreiro...")
        print("")
        jornada(classe)
    elif classe == "2":
        classe = "Mago"
        print(f"\n{nome}, você escolheu o caminho do Mago!")
        print("")
        print("Iniciando a jornada do Mago...")
        print("")
        jornada(classe)
    elif classe == "3":
        classe = "Arqueiro"
        print(f"\n{nome}, você escolheu o caminho do Arqueiro!")
        print("")
        print("Iniciando a jornada do Arqueiro...")
        print("")
        jornada(classe)
    elif classe == "4":
        classe = "Ladino"
        print(f"\n{nome}, você escolheu o caminho do Ladino!")
        print("")
        print("Iniciando a jornada do Ladino...")
        print("")
        jornada(classe)
    else:
        print("Classe inválida. Tente novamente.")
        escolha_classe()

def jornada(classe):
    print("Você a muito tempo sonha em se tornar um aventuiro.")
    print("Se aventurar por terras desconhecidas, enfrentar monstros e descobrir tesouros.")
    print(f"Por isso você treinou para se tornar um {classe} e finalmente ir em sua jornada.")
    print("Você se encontra nos portões do Reino de Vale, um reino conhecido por ser o Reino dos Aventureiros.")
    print("Um reino cheio de pessoas de diversas raças vindas de diversos lugares.")
    print("Um reino cheio de guildas e comercios, onde você pode encontrar tudo o que precisa para sua jornada.")

if __name__ == "__main__":
    nome = input("Digite seu nome, aventureiro: ")
    escolha_classe()