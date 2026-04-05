#Solicita nome e idade
nome = input("Insira seu nome ")
idade = int(input("\nInsira sua idade "))

#print do nome e idade fornecidos
print (f"\nOlá {nome} você tem {idade} anos ")

#Maior ou menos de idade 
if idade < 18:
    print("\nVocê é Menor de Idade")
else:
    print("\nVocê é Maior de idade")
