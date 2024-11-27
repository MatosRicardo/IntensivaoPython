#Exercício 2: Programa, carrinho de mercado

item = input("Qual item você quer comprar? ")
preco = float(input("Qual o preço do item? "))
quantidade = int(input("Qual a quantidade do item? "))
total = preco * quantidade

print(f"Você comprou {quantidade} {item}(s) por um total de R${total:.2f}")