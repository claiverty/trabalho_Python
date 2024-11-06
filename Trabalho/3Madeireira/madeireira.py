# Apresentação e tipos de madeiras disponiveis
print('Bem-vindos a Madeireira do Lenhador Claiverty Rodrigues dos Santos')
print('Tipos de madeira disponíveis')
print('PIN - Tora de Pinho')
print('PER - Tora de Peroba')
print('MOG - Tora de Mogno')
print('IPE - Tora de Ipê')
print('IMB - Tora de Imbuia')

# Função para escolher a madeira desejada
def escolha_tipo():
  precos = {'PIN': 100.00, 'PER': 125.00, 'MOG': 150.00, 'IPE': 175.00, 'IMB': 200.00} # Valor de cada mmadeira
  while True:
    tipo = input('Qual tipo de madeira você deseja? (PIN/PER/MOG/IPE/IMB): ').upper()
    if tipo in precos:
      return precos[tipo]
    print('Opção de madeira inválida. Tente novamente')

# Função para escolher a quantidade de madeiras e o desconto que vai ser aplicado
def qnt_toras():
  while True:
    try:
     quantidade = float(input('Qual é quantidade de toras? (em m³): '))
     if quantidade > 2000:
      print('Não aceitamos pedidos com essa quantidade de toras. Tente novamente')
     elif quantidade <= 0:
      print('Quantidade inválida. Informe o número de toras.')
     else:
       if quantidade < 100:
        desconto = 0
       elif quantidade < 500:
        desconto = 0.04
       elif quantidade < 1000:
        desconto = 0.09
       else:
        desconto = 0.16
       return quantidade, desconto
    except ValueError:
      print('Insira um valor númerico. Tente novamente')

# Função para escolher como a madeira vai ser transportada
def transporte():
  valor_transporte = {'1': 1000, '2': 2000, '3': 2500} 
  while True:
    opcao = input('Escolha o tipo de transporte (1-Rodoviário, 2-Ferroviário, 3-Hidroviário): ')
    if opcao in valor_transporte:
      return valor_transporte[opcao]
    print('Opção de tranporte inválida. Tente novamente')

# Fechando o pedido
preco_madeira = escolha_tipo()
quantidade, desconto = qnt_toras()
preco_transporte = transporte()
total = ((preco_madeira * quantidade) * (1 - desconto) + preco_transporte)

print(f'Total: R$ {total:.2f}')

