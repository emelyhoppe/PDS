servicos = ['restauração','capintaria', 'Marcenaria']

while True:
    print('0: Sair')
    print('1: Adicionar tarefa')
    print('2: Remover tarefa')
    print('3: Vizualizar tarefas atuais')

    opcoes = input('Selecione: 0, 1, 2 ou 3')

    if opcoes == '1':
        servico = input('Digite o serviço')
        servicos.append(servico)
    if opcoes == '2':
        print(servicos.pop(0))
    if opcoes == '3':
        print(f'{len(servicos)} - {servicos}')
    if opcoes == '0':
        break

