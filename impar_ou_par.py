# Função para verificar se o número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."

# Entrada do usuário
numero = int(input("Digite um número: "))

# Exibir o resultado
print(verificar_par_ou_impar(numero))