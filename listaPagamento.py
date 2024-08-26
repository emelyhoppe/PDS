pagamentos = []

while True:
    print('0: Sair.')
    print('1: Adicionar valor a ser pago.')
    print('2: Pagar valor.')
    print('3: Vizualizar valores a serem pagos.')

    opcoes = input('Digite a opção que deseja: \n')

    if opcoes == '1':
        valor = float(input("Digite seu pagamento: \n"))
        pagamentos.append(valor)
    if opcoes == '2':
        print(pagamentos[0])
        pagamento = float(input('Digite o valor a ser pago: \n'))

        if pagamento == pagamentos[0]:
            print(f'conta no valor de {pagamentos.pop(0)} efetuado \n')
        else:
            print('Valor insuficiente \n')           
    if opcoes == '3':
        print(f'{len(pagamentos)} - {pagamentos}')
    if opcoes == '0':
        break