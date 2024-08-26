atendimentos = []

while True:
    print('0: Sair.')
    print('1: Adicionar atendimento.')
    print('2: Remover atendimento.')
    print('3: Vizualizar lista de atendimentos.')

    opcoes = input('Digite a opção que deseja: ')

    if opcoes == '1':
        atendimento = input("Digite seu atendimento: ")
        atendimentos.append(atendimento)
    if opcoes == '2':
        print(atendimentos.pop(0))
    if opcoes == '3':
        print(f'{len(atendimentos)} - {atendimentos}')
    if opcoes == '0':
        break