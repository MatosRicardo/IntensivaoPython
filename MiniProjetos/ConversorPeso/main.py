weight = float(input("Entre com o seu peso"))
unidade = input("Kg ou Lbs?")

if unidade == "K":
  weight = weight * 2.205
  unidade = "Lbs"
  print(f"Seu peso é: {round(weight,1)}" + unidade)
elif unidade == "L":
  weight = weight / 2.205
  unidade = "Kg"
  print(f"Seu peso é: {round(weight,1)}" + unidade)
else: 
  print(f"{unidade} não é uma unidade válida")
  
  
