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