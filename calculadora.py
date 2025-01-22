# Importa a função necessária
from cs50 import get_int

print("Calculadora Inteligente")

# Etapa 1 - Pede que o usuário informe os números
num1 = get_int("Primeiro número: ")
num2 = get_int("Segundo número: ")

# Etapa 2 - Realiza a operação aritmética desejada
check = False

while not check:
    operation = input("Operação: ")
    check = True

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*" or operation =="x":
        operation = "*"
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        check = False

# Etapa 3 - Imprimir na tela o resultado da operação
print(num1, operation, num2, "=", result)
