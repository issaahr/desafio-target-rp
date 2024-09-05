# Requisição da string para o usuário e conversão para letras minúsculas
string = input("Digite a string para verificação: ").lower()
contagem_de_a = 0

# Verifica quantas letras "A" tem na string e incrementa o contador
for letra in string:
    if letra == "a":
        contagem_de_a += 1

# Resultado
print(f"A quantidade de letras 'a' na string {string} é: {contagem_de_a}")