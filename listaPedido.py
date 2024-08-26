pedidos = []

while True:
    print('0: Sair.')
    print('1: Adicionar pedido.')
    print('2: Remover pedido.')
    print('3: Vizualizar lista de pedidos.')

    opcoes = input('Digite a opção que deseja: ')

    if opcoes == '1':
        pedido = input("Digite seu pedido: ")
        pedidos.append(pedido)
    if opcoes == '2':
        print(pedidos.pop(0))
    if opcoes == '3':
        print(f'{len(pedidos)} - {pedidos}')
    if opcoes == '0':
        break