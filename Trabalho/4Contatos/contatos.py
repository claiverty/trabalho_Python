# Apresentação
print('Bem-vindos a lista de contatos do Claiverty Rodrigues dos Santos')

# Iniciando a lista de contatos e do id
lista_contatos = []
id_global = 4990958

# Função para cadastrar contatos
def cadastrar_contato(id):
  print('\nMENU DE CADASTRO')
  nome = input('Qual é o nome do contato: ')
  atividade = input('Qual é a atividade do contato: ')
  telefone = input('Qual é telefone do contato: ')

  contato = {
    'id': id,
    'nome': nome,
    'atividade': atividade,
    'telefone': telefone
  }

  lista_contatos.append(contato.copy())
  print('Contato salvo com sucesso!\n')

# Função apra consultar contatos
def consultar_contatos():
  while True:
    print('\nMENU DE CONTATOS:')
    print('1. Consultar Todos')
    print('2. Consultar por Id')
    print('3. Consultar por Atividade')
    print('4. Retornar ao menu')

    opcao = input('\nEscolha uma opção (1, 2, 3 ou 4): ')
    if opcao == '1': # Ver a lista de contatos
      if lista_contatos:
        for contato in lista_contatos:
          print(contato)
      else:
        print('Nenhum contato cadastrado.')   
    
    elif opcao == '2': # Encontrar o contato pelo ID
      try:
        id_consulta = int(input('Digite o ID do contato: '))
        contato_encontrado = False
        for contato in lista_contatos:
          if contato['id'] == id_consulta:
            print(contato)
            contato_encontrado = True
            break
        if not contato_encontrado:
          print('Contato não encontrado.')
      except ValueError:
        print('Id inválido. Digite um número.')

    elif opcao == '3': # Encontrar o contato pela atividade
      atividade_consulta = input('Digite a atividade: ')  
      encontrados = [contato for contato in lista_contatos if contato['atividade'] == atividade_consulta]
      if encontrados:
        for contato in encontrados:
          print(contato)
      else:
        print('Nenhum contato com essa atividade foi encontrado.')
    
    elif opcao == '4': # Voltar ao menu
      break
    
    else:
      print('Opção inválida.')

# Função para remover um contato
def remover_contato():
  while True:
    try:
      id_remover = int(input('Digite o ID do contato a ser removido: '))
      for contato in lista_contatos:
        if contato['id'] == id_remover:
          lista_contatos.remove(contato)
          print('Contato removido com sucesso.')
          return
      print('Id inválido')
    except ValueError:
      print('ID inválido. Digite um número.')  


# Menu da lista de contatos
while True:
    print('\nMENU DE CONTATOS:')
    print('1. Cadastrar Contato')
    print('2. Consultar Contato')
    print('3. Remover Contato')
    print('4. Encerrar Lista')
    opcao_menu = input('\nEscolha uma opção (1, 2, 3 ou 4): ')

    if opcao_menu == '1':
       id_global += 1
       cadastrar_contato(id_global)

    elif opcao_menu == '2':
         consultar_contatos()

    elif opcao_menu == '3':
         remover_contato()

    elif opcao_menu == '4':
         print('Lista Encerrada.')
         break

    else:
      print('Opção inválida.')     
