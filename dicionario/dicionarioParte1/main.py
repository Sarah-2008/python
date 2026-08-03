aluno = {} # vazio
aluno ['nome'] = 'Carlos'
aluno ['idade'] = 17
aluno ['nota'] = 8.5
print(aluno)

# Forma compacta
aluno2 = {'nome; Alice'
          'idade: 18'
          'nota: 4.8'}
print(aluno.get('nome'))
print(aluno.get('gmail'))
print(aluno('email', 'N/A'))

for chave, valor in aluno.itens():
    print(f'{chave}:{valor}')