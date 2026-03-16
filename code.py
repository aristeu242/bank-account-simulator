print("=== ANALISADOR DE GASTOS ===")

gastos = {}

while True:
    categoria = input("\nDigite a categoria do gasto (ou 'sair' para terminar): ")

    if categoria.lower() == "sair":
        break

    valor = float(input("Digite o valor gasto: R$"))

    gastos[categoria] = valor

total = sum(gastos.values())

maior_categoria = max(gastos, key=gastos.get)
maior_valor = gastos[maior_categoria]

print("\n=== RESUMO DOS GASTOS ===")

for categoria, valor in gastos.items():
    print(f"{categoria}: R${valor}")

print(f"\nTotal gasto: R${total}")
print(f"Maior gasto: {maior_categoria} (R${maior_valor})")