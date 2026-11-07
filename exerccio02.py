
# 2. Receba: ano de nascimento e ano atual. Calcule idade semanas
# Entrada
# anoNascimento
# anoAtual
anoNscimento = int(input("Digite o ano que você nasceu: "))
anoAtual = int(input("Digite o ano atual: "))




# Processamento
idade = anoAtual - anoNascimento
idadeSemanas = 4 * 12 * idade


# Saída
print(f"Sua idade é: {idade} ano(s)")
print(f"Sua idade em semanas: {idadeSemanas} semanas(s)")