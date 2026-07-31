# função simples sem parâmentos

def saudar():
    print('Olá! Bem vindos ao senai')
    print('Bons estudos!')

saudar() # Chamando a função
saudar() # pode chamar várias vezes

# Com parâmetros

def saudar_pessoas(nome, curso):
    print(f'Olá, {nome}')
    print(f'Bem-vindo ao curso de {curso}')

saudar_pessoas('Max', 'Python')

# Parâmetro com valor padrão

def potencia(base, expoente=2):
    return base ** expoente

print(potencia(5)) # 25 (exp padrão = 2)
print(potencia(2,8)) # 256