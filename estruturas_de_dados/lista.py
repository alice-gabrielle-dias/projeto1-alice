lista_nomes = []
while True:
    nome = input("Digite um nome ou Sair para encerrar: ")
    if nome.lower() == "sair":
        print("Obrigada! Até Logo!")
        break
    lista_nomes.append(nome)
    print(f"{nome} adicionado a lista.")
print("lista de nomes:")
print(lista_nomes)
        
