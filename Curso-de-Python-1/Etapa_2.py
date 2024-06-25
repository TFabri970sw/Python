#Se = if. Permite que você verifique uma condição e execute um bloco de código específico com base no resultado dessa condição.

#O elif é uma palavra-chave em Python que significa "else if". Ele é usado em conjunto com o if para criar uma estrutura de decisão mais complexa.

#O else é uma palavra-chave em Python que é usada em conjunto com o if e o elif para criar uma estrutura de decisão mais completa.
#Exemplo:

idade = 25

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é adulto.")
elif idade >= 65:
    print("Você é idoso.")
else:
    print("Idade inválida.")

#O tipo int no Python representa números inteiros, ou seja, números positivos, negativos ou zero, sem parte decimal
#Alguns exemplos de valores int:

#42
#-10
#0
#1000
#-5678

#Exemplos:

# Adição
print(10 + 5)  # Resultado: 15

# Subtração
print(20 - 8)  # Resultado: 12

# Multiplicação
print(3 * 7)   # Resultado: 21

# Divisão inteira (retorna apenas a parte inteira)
print(15 // 4) # Resultado: 3

# Resto da divisão
print(17 % 5)  # Resultado: 2

#Também é possível converter outros tipos de dados para int usando a função int():

# Convertendo uma string para int
numero_str = "42"
numero_int = int(numero_str)
print(numero_int)  # Resultado: 42

# Convertendo um float para int (trunca a parte decimal)
numero_float = 3.14
numero_int = int(numero_float)
print(numero_int)  # Resultado: 3

#Para definir uma função em Python, usamos a palavra-chave 'def' seguida do nome da função e dois pontos.
#exemplo:

def exibir_saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")

#usando a biblioteca 'os' para limpar o console.
#exemplo:

import os

def exibir_saudacao(nome):
    os.system('cls')
    print(f"Olá, {nome}! Seja bem-vindo(a).")
