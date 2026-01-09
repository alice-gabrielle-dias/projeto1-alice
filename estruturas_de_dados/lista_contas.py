numeros= []
while True:
    Entrada = input("Digite um número ou Sair para encerrar: ")
    if Entrada.lower() == "sair":
        break
    numero= float(Entrada)
    numeros.append(numero)
print("Números digitados:", numeros)
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))
print("Maior:", max(numeros))
print("Menor:", min(numeros))