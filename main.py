def escolha_classe():
    print("Escolha sua classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Bardo")
    print("4. Ladino")

    classe = input("Qual sua classe? (1/2/3/4): ")

    
    if classe == "1":
        classe = "Guerreiro"
        print(f"\n{nome}, você escolheu o caminho do Guerreiro!")
        print(f"\nIniciando a jornada de {nome} o Guerreiro...")
        return classe
    elif classe == "2":
        classe = "Mago"
        print(f"\n{nome}, você escolheu o caminho do Mago!")
        print(f"\nIniciando a jornada de {nome} o Mago...")
        return classe
    elif classe == "3":
        classe = "Bardo"
        print(f"\n{nome}, você escolheu o caminho do Bardo!")
        print(f"\nIniciando a jornada de {nome} o Bardo...")
        return classe
    elif classe == "4":
        classe = "Ladino"
        print(f"\n{nome}, você escolheu o caminho do Ladino!")
        print(f"\nIniciando a jornada de {nome} o Ladino...")
        return classe
    else:
        print("Classe inválida. Tente novamente.")
        escolha_classe()

def jornada():
    print("\nVocê a muito tempo sonha em se tornar um aventuiro.")
    print("Se aventurar por terras desconhecidas, enfrentar monstros e descobrir tesouros.")
    print(f"Por isso você treinou para se tornar um {classe} e finalmente ir em sua jornada.")
    print("Você se encontra nos portões do Reino de Vale, conhecido por ser o Reino dos Aventureiros.")
    print("Um reino cheio de pessoas de diversas raças, vindas de diversos lugares.")
    print("Cheio de guildas e comercios, onde você pode encontrar tudo o que precisa para sua jornada.")
    print("\nVocê entra pelos portões olhando em volta, vendo a movimentação das pessoas, as lojas, as guildas, os bares e as tavernas.")
    print("Você se sente animado e pronto para começar sua aventura, mas antes de sair para explorar o reino, você decide ir até a taverna \nmais próxima para descansar e se preparar para o que está por vir.")
    print("Até que você avista uma taverna, um lugar óbvio para adquirir informações.")
    print("\nAo empurrar a pesada porta de madeira da taverna, o cheiro de carne assada, ensopado e cerveja inunda suas narinas. O lugar, \nchamado Canto dos Bardos, está lotado.") 
    
    if classe == "Bardo":
        print("Sendo você um Bardo, o nome lhe chama bastante atenção.")
    
    print("Você ouve o som de canecas batendo, risadas altas de anões em uma mesa próxima e um grupo de bardos tocando num canto \niluminado pela lareira.")
    print("Você se aproxima do balcão, onde um taverneiro corpulento e com um tapa-olho limpa um copo de vidro com um pano duvidoso. \nOlhando ao redor, algumas coisas chamam a sua atenção, um quadro com vários papéis, o que aparenta ser uma briga entre \naventureiros e uma figura misteriosa no canto da taverna que aparentemente está com a atenção direcionada a você. \n\nVocê precisa decidir qual será o seu primeiro passo no Reino de Vale.")
    escolha_taverna()

def escolha_taverna()
    print("\nO que você fará agora?")
    print("1 - Analisar o Quadro de Avisos")
    print("2 - onversar com o Taverneiro")
    print("3 - Abordar a Figura Misteriosa")
    print("4 - Intervir na Confusão")
    escolha = input("> ")

    if escolha == "1":
        print("Você senta num banco no balcão, joga uma moeda na madeira para pedir uma bebida e decide puxar \nassunto com o taverneiro caolho. Ele parece conhecer todo mundo que entra e sai daqui.")
        print("\nTaverneiro - Hm? Eu nunca vi seu rosto por aqui, por acaso é novo na cidade?")
        print("\n")
    elif escolha == "2":
        print("")
    elif escolha == "3":
        print("")
    elif escolha == "4":
        print("")

if __name__ == "__main__":
    nome = input("Digite seu nome, aventureiro: ")
    classe = escolha_classe()
    jornada()