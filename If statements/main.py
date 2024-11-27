# Condicional if-elif-else para verificar a idade do usuário

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você agora está cadastrado!")
elif idade < 0:
    print("Você ainda não nasceu!")
elif idade >= 100:
    print("Você está velho demais para se inscrever.")
else:
    print("Você precisa ter 18 anos ou mais para se inscrever.")
