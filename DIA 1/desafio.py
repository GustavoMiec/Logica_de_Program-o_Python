"""
Lógica de Programação – Dia 1: Condicionais (if, elif, else)
1. O que são condicionais?
Condicionais são estruturas que permitem que o programa tome decisões baseadas em certas condições. Por exemplo:

Se o usuário for maior de idade, pode entrar no site.

Se a nota for maior ou igual a 7, o aluno passou.

2. Sintaxe básica em Python
"""
if condição1:
    # bloco de código se condição1 for verdadeira
elif condição2:
    # bloco de código se condição1 for falsa e condição2 verdadeira
else:
    # bloco de código se nenhuma condição anterior for verdadeira
    
"""
Importante:

O if é obrigatório.

Você pode ter zero ou vários elif.

O else é opcional.

A indentação (espaços antes do código) é fundamental no Python.

3. Exemplos simples
"""

# Exemplo 1: Verificar se um número é positivo, negativo ou zero
num = int(input("Digite um número: "))

if num > 0:
    print("Número positivo")
elif num == 0:
    print("Número é zero")
else:
    print("Número negativo")

# Exemplo 2: Verificar se a idade permite votar
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar ainda")

"""
4. Dicas importantes
Use operadores relacionais: >, <, ==, !=, >=, <= para construir as condições.

As condições são avaliadas na ordem. Assim que uma condição verdadeira for encontrada, o restante é ignorado.

Pode aninhar if dentro de outros if se precisar de decisões mais complexas.

Desafios do Dia 1
"""

# 🔹 Desafio 1 - par ou ímpar
# Peça para o usuário digitar um número inteiro e informe se ele é par ou ímpar.

# 🔹 Desafio 2 - próximo ímpar
# O usuário digita um número e o programa retorna o próximo número ímpar.
# Se o número já for ímpar, retorna ele mesmo.
# Se o número for par, retorna o próximo ímpar (ou seja, n + 1).

# 🔹 Desafio 3 - idade
# Faça um programa que receba a idade e diga se a pessoa é:
# Criança (0 a 12 anos)
# Adolescente (13 a 17)
# Adulto (18 a 64)
# Idoso (65+) 

# 🔹 Desafio 4 - média
# Peça para o usuário digitar 3 notas, calcule a média e informe se ele passou (média ≥ 7), recuperação (média entre 5 e 7) ou reprovado (média < 5).

# 🔹 Desafio 5 - média
# Escreva um programa que receba uma letra do alfabeto e diga se é uma vogal ou consoante.

# 🔹 Desafio 6 - calculadora 
# Faça uma calculadora simples: o usuário digita dois números e a operação (+, -, *, /). O programa deve mostrar o resultado correto. Caso a operação seja inválida, mostre uma mensagem de erro.

#🔹 Desafio 7 – Triângulo válido?
#Peça três números que representam lados de um triângulo e diga se formam ou não um triângulo válido.
#(Regras: a soma de dois lados sempre tem que ser maior que o terceiro.)
# 🧠 Se for válido, diga também se é:
#Equilátero (3 lados iguais)
# Isósceles (2 lados iguais)
# Escaleno (3 lados diferentes)

#🔹 Desafio 8 – Ano bissexto
# Peça um ano ao usuário e diga se ele é bissexto.
# 📌 Regras:
# É bissexto se for divisível por 4 e não por 100, ou divisível por 400.

#🔹 Desafio 9 – Maior número
# Peça 3 números diferentes ao usuário e diga qual é o maior deles.

# 🔹 Desafio 10 – Loja de desconto
# Peça o valor total de uma compra.
# Se for maior ou igual a 100, dê 10% de desconto.
# Caso contrário, diga que não há desconto.
# Mostre o valor final.

# 🔹 Desafio 11 – Verificador de senha
# Peça ao usuário uma senha.
# Se a senha for igual a "python123" (ou qualquer senha que você definir), diga "Acesso permitido", senão "Acesso negado".