temperatura = [32.2, 31.1, 29.0, -10.0, 54.2, 0.0]

# cálculos usando funções
media = sum(temperatura) / len(temperatura)
maxima = max(temperatura)
minima = min(temperatura)

# conta quantos dias ficaram acima da media
acima = 0
for temp in temperatura:
    if temp > media:
        acima += 1

# ordem crescente
ordem = sorted(temperatura)

print (f'Temperaturas registradas: {temperatura}')
print('=========Relatório Climático=========')
print(f'Média: {media:.2f}°C')
print(f'Máxima: {maxima:.2f}°C')
print(f'Mínima: {minima:.2f}°C')
print(f'Dias acima da Média: {acima}')
print(f'Em ordem crescente: {ordem}')