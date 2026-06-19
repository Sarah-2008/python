# Solicita o primeiro número ao usuário
num1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número ao usuário
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação foi escolhida e realiza o cálculo
if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif operacao == "/":
    # Verifica se o divisor é zero
    if num2 == 0:
        print("Erro: não é possível dividir por zero.")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado:.2f}")

# Caso a operação digitada seja inválida
else:
    print("Erro: operação inválida. Utilize apenas +, -, * ou /.")