# input() = Uma função que solicita ao usuário que insira dados  
#           Retorna os dados inseridos como uma string, segue os mesmos padrão do Js


name = input("Qual é o seu nome? ")
age = int(input("Qual é a sua idade? "))
age = int(age)
age += 1

print(F"Olá, {name}")
print(F"Você tem {age} anos")

