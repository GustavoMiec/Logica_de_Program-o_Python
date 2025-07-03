# Dia 2 – Operadores Lógicos e Condicionais Compostas
"""
Operadores Lógicos
Os operadores lógicos são usados para juntar condições e criar testes mais complexos. Eles retornam True ou False.

1. and (E lógico)
Retorna True se TODAS as condições forem verdadeiras.
Exemplo:
"""
idade = 20  
tem_cnh = True  
if idade >= 18 and tem_cnh:  
    print("Pode dirigir")  
    
#Aqui, só pode dirigir se for maior ou igual a 18 e tiver carteira.

#__________________________________________________________________________________________________________________________________________________________________________________________________________________

"""
2. or (OU lógico)
Retorna True se PELO MENOS UMA condição for verdadeira.
Exemplo:
"""
dia = "domingo"  
if dia == "sábado" or dia == "domingo":  
    print("Fim de semana")  

# Aqui, se o dia for sábado ou domingo, imprime “Fim de semana”.
#__________________________________________________________________________________________________________________________________________________________________________________________________________________
"""
3. not (NÃO lógico)
Inverte o valor lógico. Se for True, vira False. Se for False, vira True.
Exemplo:
"""
ligado = False  
if not ligado:  
    print("Apagado")  
#Se o aparelho não estiver ligado, imprime “Apagado”.
#__________________________________________________________________________________________________________________________________________________________________________________________________________________
"""
Exemplos combinados
Você pode combinar vários operadores para criar condições mais complexas, usando parênteses para organizar a lógica:
"""
idade = 20
tem_cnh = True
tem_autorizacao = False

if idade >= 18 and (tem_cnh or tem_autorizacao):
    print("Pode dirigir")
else:
    print("Não pode dirigir")

#__________________________________________________________________________________________________________________________________________________________________________________________________________________

# 10 Desafios – Dia 2

# 1. Voto obrigatório
# Peça a idade do usuário. Se a idade for maior ou igual a 18 e menor que 65, diga “Voto obrigatório”. Caso contrário, diga “Voto facultativo”.

# 2. Acesso liberado
# Peça uma senha e um status “ativo” (True ou False). O acesso só é liberado se a senha for correta ("abc123") e o status for True.

# 3. Fim de semana
# Peça o dia da semana e diga se é fim de semana (sábado ou domingo).

# 4. Número entre 10 e 20
# Peça um número e diga se ele está entre 10 e 20 (inclusive).

# 5. Negação
# Peça uma resposta “sim” ou “não”. Se a resposta for diferente de “sim”, use not para imprimir “Resposta negativa”.

# 6. Idade para bebida
# Peça a idade e diga se a pessoa pode beber legalmente (idade maior ou igual a 18).

# 7. Maioridade ou emancipação
# Peça a idade e um status de emancipação (True/False). A pessoa é considerada adulta se tiver 18 anos ou mais ou se for emancipada.

# 8. Login com restrição
# Peça o usuário, senha e um status de “bloqueado” (True/False). O login só acontece se a senha estiver correta e o usuário não estiver bloqueado.

# 9. Número par ou maior que 10
# Peça um número. Imprima “Aceito” se o número for par ou maior que 10.

# 10. Validar idade para festa
# Peça a idade. Se a idade for maior que 18 e não for menor que 60, permita entrada; caso contrário, negue.





