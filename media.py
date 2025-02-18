# Exercício:
# Crie um programa em Python que solicite ao usuário quatro notas, calcule a média deles e exiba o resultado.


# Função Calcula a média
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Função mostra se foi aprovado ou reprovado
def aprovar_reprovar(media):
    if media >= 6:
        return f"Aluno aprovado!"
    else:
        return f"Aluno reprovado!"


numeros = [] # Cria uma lista

# Cria um loop pedindo as notas ao usuário
for i in range(4):
    while True:
        try:
            num = float(input(f"Digite a {i+1}ª nota: "))
            numeros.append(num)
            break
        except ValueError:
            print("Digite uma nota valida!")


media = calcular_media(numeros) # Armazenar a média em uma variável

# Chamar a função aprovar_reprovar() e exibir o resultado
print(f"\nA média do aluno: {media:.2f}")
print(aprovar_reprovar(media))