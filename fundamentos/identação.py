# Exemplo funcional de indentação em Python
# Demonstra função, condicional e classe em um fluxo simples

import time

def pensar_por_10_segundos():
    print("Pensando...")
    time.sleep(3)  # reduzido para não travar muito
    print("Lembrei!")

def verificar_numero(numero):
    if numero > 5:
        print(f"{numero} é maior que 5")
    else:
        print(f"{numero} é menor ou igual a 5")

class BemVindo:
    def __init__(self, nome):
        print(f"Bem-vinda, {nome}!")

def main():
    nome = input("Digite seu nome: ")
    numero = int(input("Digite um número: "))

    pensar_por_10_segundos()
    verificar_numero(numero)
    BemVindo(nome)

if __name__ == "__main__":
    main()
