print ('Sistema desenvolvido por Claiverty Rodrigues dos Santos')

# Valor do plano e idade do cliente
valorBase = float(input('Qual é o valor base do plano de saúde? '))
idade = int(input('Qual é a idade do cliente: '))

# Aplicando a % de acordo com a idade
if 0 <= idade < 19:
  porcentagem = 100 / 100 # Abaixo de 19 anos, paga 100% do valor base

elif 19 <= idade < 29:
  porcentagem = 150/100 # Entre 19 e 28 anos, paga 150% do valor base

elif 29 <= idade < 39:
  porcentagem = 225/100 # Entre 29 e 38 anos, paga 225% do valor base

elif 39 <= idade < 49:
  porcentagem = 240/100 # Entre 39 e 48 anos, paga 240% do valor base

elif 49 <= idade < 59:
  porcentagem = 350/100 # Entre 49 e 58 anos, paga 350% do valor base

else:
  porcentagem = 600 / 100 # Acima dos 59 anos, paga 600% do valor base

 # Valor mensal do plano
valorMensal = valorBase * porcentagem

# Resultado do código
print('O cliente com', idade, 'anos irá pagar um valor de R$', round(valorMensal, 2), 'por mês.')