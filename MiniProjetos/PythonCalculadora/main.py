operador = input("Digite um operador (+ - * /): ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2
    print("Resultado: ", resultado)
elif operador == "-":
    resultado = num1 - num2
    print("Resultado: ", resultado)
elif operador == "*":
    resultado = num1 * num2
    print("Resultado: ", resultado)
elif operador == "/":
    resultado = num1 / num2
    print("Resultado: ", resultado)
else:
    print("Operador inválido")