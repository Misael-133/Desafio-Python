#Usuário insere Informações (Nome, Idade e Salário)
nome = input("insira seu nome ")
idade = int(input("\nInsira sua idade "))
salario = float(input("\nInsira seu Salário "))

#print das informações fornecidas
print(f"\nOlá {nome}, você tem {idade} anos e recebe atualmente R${salario:.2f}")

#Verificação de classificação de renda
if salario < 2000:
    print("\nAtualmente você é Baixa Renda")
elif salario <= 5000:
    print("\nAtualmente você é Média Renda")
elif salario > 5000:
    print("\nAtualmente você é Alta Renda")
