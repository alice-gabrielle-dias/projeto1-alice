# Função para somar dois números
def somar(x, y):
    return x + y

# Função para subtrair dois números
def subtrair(x, y):
    return x - y

# Função para multiplicar dois números
def multiplicar(x, y):
    return x * y

# Função para dividir dois números
def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

# Função principal para interagir com o usuário
def calculadora():
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"{numero1} + {numero2} = {somar(numero1, numero2)}")
    elif escolha == '2':
        print(f"{numero1} - {numero2} = {subtrair(numero1, numero2)}")
    elif escolha == '3':
        print(f"{numero1} * {numero2} = {multiplicar(numero1, numero2)}")
    elif escolha == '4':
        print(f"{numero1} / {numero2} = {dividir(numero1, numero2)}")
    else:
        print("Opção inválida")

# Executar a calculadora
calculadora()