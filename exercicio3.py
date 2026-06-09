#Escrever um programa que o usuario digita um numero de 1 até 20.
#O programa devera fazer uma contagem regressiva;
#Não permitir que op usuario digite numero maior que 20 ou menor que 1.
#Imprimir uma mensagem de "Acabou a contagem" no final.
#Não permitir digitar letras.

numero = int(input("Digite um número de 1 a 20: "))

for i in range (numero):
    print(f"{numero - i}")

print("Acabou a contagem")