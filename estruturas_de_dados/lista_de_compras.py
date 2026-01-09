lista_compras = []
while True:
    item = input("Digite um item para acrescentarmos a lista de compras ou 'Finalizar' para encerrar: ")
    if item.lower() == "finalizar":
        print("Compra finalizada! Volte sempre!")
        break
    lista_compras.append(item)
    print(f"{item} adicionado")
print("Suas compras:")
print(lista_compras)