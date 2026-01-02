tarefas = []

while True:
    try:
        print('1. Adicionar tarefa')
        print('2. Ver tarefas')
        print('3. Remover')
        print('4. Sair')

        escolha = int(input('Escolha uma das opções acima: '))

        if escolha == 1:
            esc_tarefa = input('Digite o nome da tarefa desejada: ')
            tarefas.append(esc_tarefa)
            print('Tarefa adicionada com sucesso!')

        elif escolha == 2:

                if len(tarefas) == 0:
                    print('Você ainda não tem nenhuma tarefa!')

                else: 
                    for i in range(len(tarefas)):
                        numeracao = i + 1 
                        print(f'{numeracao}. {tarefas[i]}') 

        elif escolha == 3:
            remover = input('Digite o nome do item que deseja remover: ')

            if remover in tarefas:
                tarefas.remove(remover)
                print('Item removido com sucesso!')

            else:
                print('Item não encontrado!')


        elif escolha == 4:
            print('Encerrando programa...')
            break

        else:
            print('Escolha uma das 3 opções!')

    except ValueError:
        print('Escolha uma das 3 opções!')


