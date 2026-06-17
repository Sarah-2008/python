# Coleta de dados do usuário

nome = input("Digite seu nome completo: ")

idade = int(input("Digite sua idade: "))

ano_inicio = int(input("Ano em que começou a estudar programação: "))

linguagem = input("Qual sua linguagem de programação favorita? ")

nota_satisfacao = float(
    input("Nota de satisfação com o curso (0 a 10): ")
)

anos_estudando = 2026 - ano_inicio

print("=" * 44)
print("FICHA DO DESENVOLVEDOR")
print("=" * 44)

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Anos estudando: {anos_estudando} ano(s)")
print(f"Linguagem fav.: {linguagem}")
print(f"Satisfação: {nota_satisfacao}")

print("=" * 44)