# projetos 
# Sistema simples de aluguel de carros com verificação de idade

print("=== Sistema de Aluguel de Carros ===\n")

nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))


if idade < 18:
    print("\n Desculpe, o cliente não pode alugar um carro por ser menor de idade.")
else:

    modelo = input("Infrme o modelo do carro (Sedan, SUV, Hatch, Minivan, Picape): ")
    placa = input("Digite a placa do carro: ")
if modelo == "Sedan":
        valor_diaria = 150.00
        modelo = "Sedan"
elif modelo == "SUV":
        valor_diaria = 175.00
        modelo = "SUV"
elif modelo == "Hatch":
        valor_diaria = 145.00
        modelo = "Hatch"
elif modelo == "Minivan":   
        valor_diaria = 170.00
        modelo = "Minivan"
elif modelo == "Picape":    
        valor_diaria = 180.00
        modelo = "Picape"
else:
           print("Modelo de carro inválido. Por favor, selecione um modelo válido.")        
                   
dias = int(input("Por quantos dias o carro será alugado? "))


valor_total = valor_diaria * dias

    # Exibição 
print("\n--- Resumo do Aluguel ---")
print(f"Nome do cliente: {nome}")
print(f"Idade: {idade} anos")
print(f"Placa do carro: {placa}")
print(f"Dias de uso: {dias}")
print(f"Valor da diária: R$ {valor_diaria:.2f}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")

print("\n✅ Obrigado por utilizar nosso sistema!")