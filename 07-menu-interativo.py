# Inicialização das variáveis globais para armazenar totais e contadores
total_dia = 0
total_km = 0
quant_corridas = 0

# Loop principal do menu interativo, executado indefinidamente até o usuário escolher sair
while True:
    # Exibição das opções do menu para o usuário
    print('1 - Registrar corrida')
    print('2 - Exibir total do dia')
    print('3 - Exibir total de km rodados')
    print('4 - Exibir média por corrida')
    print('5 - Resumo do dia')
    print('6 - Sair')
    
    # Captura da opção escolhida pelo usuário
    opcao = input('Escolha uma opção: ')
    
    # Verificação se a opção é registrar corrida
    if opcao == '1':
        # Solicitação dos dados da corrida: distância em km e tempo em minutos
        km = float(input('Digite a distância da corrida em km: '))
        tempo = int(input('Digite o tempo da corrida em minutos: '))
        
        # Validação para garantir que distância e tempo sejam positivos
        if km <=0 or tempo <= 0:
            print('⚠️ Distância e tempo devem ser maiores que zero. Tente novamente.')
            continue
        
        # Cálculo do valor da corrida baseado na fórmula fornecida
        valor_corrida = (2.50 * km) + (0.30 * tempo)
        
        # Atualização dos totais acumulados
        total_dia += valor_corrida
        total_km += km
        quant_corridas += 1
        
        # Exibição do valor da corrida registrada
        print(f'💰 Corrida registrada: R$ {valor_corrida:.2f}')
    
    # Verificação se a opção é exibir total do dia
    elif opcao == '2':
        print(f'Total do dia: R$ {total_dia:.2f}')
    
    # Verificação se a opção é exibir total de km rodados
    elif opcao == '3':
        print(f'Total de km rodados: {total_km:.2f} km')
    
    # Verificação se a opção é exibir média por corrida
    elif opcao == '4':
        # Verificação se há corridas registradas para calcular a média
        if quant_corridas > 0:
            media = total_dia / quant_corridas
            print(f'Média por corrida: R$ {media:.2f}')
        else:
            print('Nenhuma corrida registrada.')
    
    # Verificação se a opção é exibir resumo do dia
    elif opcao == '5':
        print('📊 Resumo do dia:')
        print(f'Quantidade de corridas: {quant_corridas}')
        print(f'Valor total do dia: R$ {total_dia:.2f}')
        print(f'Total de km rodados: {total_km:.2f} km')
        # Verificação se há corridas para incluir a média no resumo
        if quant_corridas > 0:
            media = total_dia / quant_corridas
            print(f'Média por corrida: R$ {media:.2f}')
        else:
            print('Nenhuma corrida registrada.')
    
    # Verificação se a opção é sair do programa
    elif opcao == '6':
        print('Encerrando o programa. Até mais! 👋🏾')
        break
    
    # Caso a opção seja inválida, exibe mensagem de erro
    else:
        print('❌Opção inválida. Tente novamente. 🔁')