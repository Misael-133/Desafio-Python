#Solicita Informações do Usuário
km = float(input('Insira a Distancia percorrida (km) ' ))
minuto = int(input("Insira o tempo da corrida (minutos)"))

#Cálculo de valor da corrida
vc = (2.5 * km) + (0.30 * minuto)

#Print valor da Corrida
print(f'\nO valor da corrida é de R$ {vc:.2f}')

#Verifica a Condição da corrida
if vc < 10:
    print('Corrida Ruim')
elif vc <= 20:
    print('Corrida ok')
else:
    print('Corrida Boa')