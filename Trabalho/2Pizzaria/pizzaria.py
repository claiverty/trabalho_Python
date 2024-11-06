# Apresentação e cardápio
def bem_vindo():
  print('|Bem-vindos à Pizzaria do Claiverty Rodrigues dos Santos|')
  print('====================== Cardápio ==========================')
  print('|   Tamanho  |  Pizza Salgada (PS) |   Pizza Doce (PD)   |')
  print('|      P     |      R$ 30.00       |     R$ 34.00        |')
  print('|      M     |      R$ 45.00       |     R$ 48.00        |')
  print('|      G     |      R$ 60.00       |     R$ 66.00        |')
  print('==========================================================')

# Preço das pizzas conforme o tamanho e se é doce ou salgada
precos = {'P': {'ps': 30.00, 'pd': 34.00}, 'M': {'ps': 45.00, 'pd': 48.00}, 'G': {'ps': 60.00, 'pd': 66.00}}

# Função para iniciar o pedido das pizzas
def pedir_pizza():
  total = 0
  while True:
    sabor = input('Qual sabor você deseja? (PS/PD): ').lower()
    if sabor not in ['ps', 'pd']:
        print('Sabor inválido. Tente novamente') # Aparece caso ele escolha um sabor inválido
        continue

    tamanho = input('Qual tamanho você deseja? (P/M/G): ').upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente') # Aparece caso ele escolha um tamanho inválido
        continue

    total += precos[tamanho][sabor]
    print(f'Pizza {tamanho} {sabor.upper()} adicionada. Valor: R$ {precos[tamanho] [sabor]:.2f}')

    if input('Deseja mais alguma coisa? (s/n): ').lower() != 's': # Para o cliente decidir ser quer mais pizzas ou não
       break
    
    # Fechando o pedido
  print(f'\nValor total do pedido: R$ {total:.2f}')

bem_vindo()
pedir_pizza()

        
