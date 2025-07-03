
# 🔹 Desafio 1 - par ou ímpar
# Peça para o usuário digitar um número inteiro e informe se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")
    
# 🔹 Desafio 2 - próximo ímpar
# O usuário digita um número e o programa retorna o próximo número ímpar.
# Se o número já for ímpar, retorna ele mesmo.
# Se o número for par, retorna o próximo ímpar (ou seja, n + 1).

num_par_impar = int(input("Digite um numero: "))

if num_par_impar % 2 == 0:
    numero_impar = num_par_impar + 1
    print(f"O número ímpar retornado é: {numero_impar}")
else:
    print(f"O número ímpar retornado é: {num_par_impar} ")
        
# 🔹 Desafio 3
# Faça um programa que receba a idade e diga se a pessoa é:
# Criança (0 a 12 anos)
# Adolescente (13 a 17)
# Adulto (18 a 64)
# Idoso (65+) 

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif  13 <= idade <= 17:
    print("adolecente")
elif  18 <= idade <= 64:
    print("Adulto")
else:
    print("Idoso")
    
# 🔹 Desafio 4
# Peça para o usuário digitar 3 notas, calcule a média e informe se ele passou (média ≥ 7), recuperação (média entre 5 e 7) ou reprovado (média < 5).

n1 = int(input("digite a primera nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")

# 🔹 Desafio 5
# Escreva um programa que receba uma letra do alfabeto e diga se é uma vogal ou consoante.

letra = input("Digite uma letra: ").upper()

if letra in "AEIOU":
    print("Vogal")
else:
    print("Consoante")
    
# 🔹 Desafio 6
# Faça uma calculadora simples: o usuário digita dois números e a operação (+, -, *, /). O programa deve mostrar o resultado correto. Caso a operação seja inválida, mostre uma mensagem de erro.

caracteris = str(input("Digite um operador matematico + - * /: "))

numero1 = int(input("Digite o Primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if caracteris == '+':
    print("Resutado é: ", numero1 + numero2)
elif caracteris == '-':
    print("Resutado é: ", numero1 - numero2)
elif caracteris == '*':
    print("Resutado é: ", numero1 * numero2)
elif caracteris == '/':
    print("Resutado é: ", numero1 / numero2)
else:
    print("Digite um operado matematico valido")
    
    
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

