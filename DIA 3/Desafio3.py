# Lógica de Programação – Dia 3: Laços de Repetição com while

"""
1. O que é o while?
while é um comando que repete um bloco de código enquanto uma condição for verdadeira.

Estrutura básica:
"""
while condição:
    # bloco que será repetido

# O código dentro do while fica executando até a condição virar False.

#__________________________________________________________________________________________________________________________________________________________________________________________________________________

# 2. Exemplo simples:

contador = 0

while contador < 5:
    print(contador)
    contador += 1  # aumenta o contador para sair do loop

#Esse código vai imprimir os números de 0 até 4.

#__________________________________________________________________________________________________________________________________________________________________________________________________________________
"""
3. Importante: Evitar loops infinitos
Se a condição nunca virar falsa, o programa fica preso repetindo o código para sempre. Por isso, sempre atualize a variável da condição dentro do while.
"""
#__________________________________________________________________________________________________________________________________________________________________________________________________________________
"""
4. Usos comuns do while
Repetir uma pergunta até o usuário responder corretamente.

Fazer um menu interativo que só sai quando o usuário pedir.

Processar dados até uma condição de parada.
"""
#__________________________________________________________________________________________________________________________________________________________________________________________________________________
5. Exemplos práticos
Pedir senha até acertar:

senha_correta = "python123"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso liberado!")

#__________________________________________________________________________________________________________________________________________________________________________________________________________________

# 1. Senha até acertar
# Peça uma senha ao usuário. Enquanto a senha digitada for diferente de "python123", continue pedindo.
# Quando acertar, mostre: “Acesso liberado”.

# 2. Soma até 0
# Peça vários números. Some todos até o usuário digitar 0.
# No final, mostre a soma total.

# 3. Número positivo
# Peça números ao usuário até ele digitar um número negativo.
# Para cada número positivo digitado, imprima: “Número aceito”.

# 4. Validação de número entre 1 e 10
# Peça ao usuário um número entre 1 e 10.
# Enquanto ele digitar algo fora desse intervalo, repita a pergunta.

# 5. Contador de tentativas
# Peça um número secreto (ex: 7).
# O usuário deve tentar adivinhar o número.
# Conte quantas tentativas ele usou até acertar.

# 6. Calculadora simples com validação de operador
# Peça dois números e um operador (+, -, *, /).
# Enquanto o operador for inválido, repita a pergunta.
# Depois, mostre o resultado da operação.

# 7. Menu interativo
# Crie um menu que repita até o usuário digitar "3" para sair:
# 1 - Dizer Olá
# 2 - Mostrar uma dica
# 3 - Sair

# 8. Contar de 1 a N
# Peça um número N e use while para contar de 1 até N.

# 9. Verificador de par/ímpar até 0
# Peça números ao usuário.
# Para cada um, diga se é par ou ímpar.
# Pare quando o número digitado for 0.

# 10. Cadastro de nomes
# Peça o nome de várias pessoas.
# O programa só para quando o usuário digitar “sair”.
# No final, mostre quantos nomes foram cadastrados.