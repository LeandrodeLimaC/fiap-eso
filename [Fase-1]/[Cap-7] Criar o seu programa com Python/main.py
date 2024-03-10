def ask(message: str):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Valor inválido")


qtd_anos = ask("Há quantos anos você fuma? ")
valor_maco = ask("Qual o valor do maço? R$ ")
qtd_macos_por_dia = ask("Quantos maços você fuma por dia? ")

total_dias = qtd_anos * 365
valor_total = total_dias * qtd_macos_por_dia * valor_maco

if valor_total < 20000:
    print(f'Com o valor R$ {valor_total:.2f}, você poderia ter dado entrada em um carro.')
elif valor_total <= 50000:
    print(f"Com o valor R$ {valor_total:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {valor_total:.2f}, você poderia ter comprado um carro zero.")
