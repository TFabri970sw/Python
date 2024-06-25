#Exibir uma mensagem no terminal.
print('Hello Word!\n')
print('Hi, My name is Thiago Fabri')
print('Im 17 years old')
print('Today is a thursday')
print('Saint Anthony holiday')
print('Today is the first day of Python studies')
print('wish me luck')

#Permite pular uma linha.
#Se colocar na frente da palavra pula uma linha para cima é no final da palavra pula uma linha para baixo.
#Exp...
print('\nPular linha cima')
print('Pular linha baixo\n')
print('Exenplo')

#As variáveis são utilizadas para armazenar dados durante a execução de um programa.
#Elas atuam como "caixas" que podem conter diferentes tipos de informações, como números, textos, listas, entre outros.
#Atribuição de valores: Para criar uma variável, basta atribuir um valor a ela usando o operador de atribuição =. Por exemplo: nome = "Thiago".
nome = 'Thiago'
#usar letras minúsculas e separar as palavras com underscores (_). Isso torna o código mais legível e fácil de entender.
nome_e_sobrenome = 'Thiago Fabri'

#Também podemos usar 3 aspas dupla para a quebra de linha.
print("""Explore the world!
      """)

#f-string (format string) é uma maneira conveniente e eficiente de formatar strings.
#Elas permitem que você insira expressões Python dentro de strings formatadas, facilitando a criação de strings com valores dinâmicos de forma mais legível e concisa.
#f-string, você utiliza o prefixo f ou F antes das aspas que delimitam a string.
#Dentro da string, você pode então colocar variáveis, expressões ou até mesmo chamadas de função Python entre chaves {}.
nome = 'Thiago'
idade = 17
altura = 1.75

# Exemplo de f-string
mensagem = f"Olá, meu nome é {nome}, eu tenho {idade} anos e minha altura é {altura} metros."
print(mensagem)

#Permite que o usuario esscreva no terminal.
input()