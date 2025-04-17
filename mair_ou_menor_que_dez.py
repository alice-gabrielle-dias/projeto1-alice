# Função para verificar se o número é maior ou menor que 10
def verificar_maior_ou_menor_que_10(numero):
    if numero > 10:
        return f"{numero} é maior que 10."
    elif numero < 10:
        return f"{numero} é menor que 10."
    else:
        return f"{numero} é igual a 10."

# Entrada do usuário
numero = float(input("Digite um número: "))

# Exibir o resultado
print(verificar_maior_ou_menor_que_10(numero))