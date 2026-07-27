alunos = ['Carlos', 'Ana', 'Diana', 'Bruno']
        #   0         1        2        3

# append, insert, remove, pop
alunos.append('Eduardo')
#                4
alunos.insert(0, 'Alice') #escolher a posição do item
alunos.remove('Diana')

ultimo = alunos.pop()
print(alunos, '| removido:', ultimo)

# sort vs sorted
alunos.sort()  # modifica no lugar

nova = sorted(alunos, reverse=True) # cria outra lista

print(alunos)