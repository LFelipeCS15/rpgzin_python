def inicio():
    print("Escolha sua classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Arqueiro")
    print("4. Ladino")

    classe = input("Qual sua classe? (1/2/3/4): ")

    
    if classe == "1":
        caminho_do_guerreiro()
    elif classe == "2":
        caminho_do_mago()
    elif classe == "3":
        caminho_do_arqueiro()
    elif classe == "4":
        caminho_do_ladino()
    else:
        print("Classe inválida. Tente novamente.")
        inicio()

def caminho_do_guerreiro():
    print(f"\n{nome} escolheu a classe de Guerreiro!")

def caminho_do_mago():
    print(f"\n{nome} escolheu a classe de Mago!")

def caminho_do_arqueiro():
    print(f"\n{nome} escolheu a classe de Arqueiro!")

def caminho_do_ladino():
    print(f"\n{nome} escolheu a classe de Ladino!") 
    

if __name__ == "__main__":
    nome = input("Digite seu nome, aventureiro: ")
    inicio()