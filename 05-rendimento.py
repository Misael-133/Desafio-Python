#Solicita Informações do Usuário
km = float(input('Insira a quantidade de km '))
tempo = int(input('Insira o tempo da corrida '))

#Evita erro
if km == 0 or tempo == 0:
    print('❌Erro: Valores não podem ser zero')

# Cálculo da corrida
valor_corrida = (2.5 * km) + (0.30 * tempo)

#Cálculo valor por km e valor por min
valor_km = valor_corrida / km
valor_min = valor_corrida / tempo

#Exibe valor 
print(f'\n💰 Valor da corrida: R$: {valor_corrida:.2f}')
print(f'R$/km: {valor_km:.2f}')
print(f'R$/min: {valor_min:.2f}')

#Condicional se vale a pena ou não
if valor_km < 1.50:
    print('❌NÃO COMPENSA')
else:
    print('✅COMPENSA')
