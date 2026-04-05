#Pergunta quantas corridas foram feitas
quant = int(input('Quantas corridas foram feitas hoje ? ' ))
total_dia = 0
total_km = 0
valor_media = 0
nao_compensa = 0
compensa = 0
mais_cara = None
mais_barata = None
#Loop For e calculo de cada corrida
for i in range (quant):
    print(f'\nCorrida {i+1}')

    km = float(input('km: '))
    tempo = int(input('Tempo: '))

    valor = (2.5*km) + (0.30 * tempo)
 

    # verifica se a corrida compensa ou não
    if valor == 0 or km == 0:
        print('❌ERRO: Valores não podem ser zero')
    elif valor / km < 1.50:
        print('❌NÃO COMPENSOU')
        nao_compensa += 1
    else:
        print('✅COMPENSOU')
        compensa += 1

    total_dia += valor #valor total ganho $
    total_km += km #quantidade de Km percorrido
    if mais_cara is None or valor > mais_cara:
        mais_cara = valor
    if mais_barata is None or valor < mais_barata:
        mais_barata = valor
    
#Cálculo do valor médio por km, evitando divisão por zero
if total_km > 0:
    valor_media = total_dia / total_km #valor médio por km
else:
    valor_media = 0 #evita divisão por zero
#print com o resultado do dia 
print(f'\nTotal de corridas feitas: {quant}')
print(f'Total ganho no dia: R$ {total_dia:.2f}')
print(f'Total de km rodados: {total_km:.2f}')
print (f'A média de valor por km foi de: R$ {valor_media:.2f}')
print(f'Quantidade de corridas que não compensaram ❌: {nao_compensa}')
print(f'Quantidade de corridas que compensaram ✅: {compensa}')
print(f'Valor da corrida mais cara: R$ {mais_cara:.2f}')
print(f'Valor da corrida mais barata: R$ {mais_barata:.2f}')
