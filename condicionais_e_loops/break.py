while True:
    nome = input("Digite um nome ou Sair para encerrar: ")
    if nome.lower() == "sair":
        print("Obrigada! Até Logo!")
        break
    print(f"Adicionado a lista: {nome}")