'''Crie um scrpt python, que leia o nome de uma pessoa
e mostre a mensagem de boas-vindas de acordo com o valor digitado'''
nome = input('Qual é o seu nome? ')
print ('Olá, ', nome, 'seja bem-vindo ao Python!' )
#-------------------------------------------------------------------
'''Crie um script Python que leia o mês do ano de nascimento de uma
pessoa e mostre uma mensagem com a data formatada'''
ano = input('Qual ano você nasceu? ')
mes = input('Qual mês você nasceu?? ')
dia = input('Que dia você nasceu? ')
print ('Você nasceu em: ', dia,'/', mes,'/', ano)
#-------------------------------------------------------------------
print ('Você nasceu no dia ', dia, 'de ', mes, 'de' , ano, '. Correto?')
#-------------------------------------------------------------------
'''Crie um script Python que leia dois numeros e tente mostrar a 
soma entre eles'''
num1 = int(input('Digite o primero numero da soma desejeda: '))
num2 = int(input('Digite o segundo numero da soma desejeda: '))
# int(input) 'diz' para o input que os valores adicionados são números inteiros
num3 = (num1 + num2)
print(num1, '+', num2, '= ', num3)
#-------------------------------------------------------------------
n = input('Digite algo: ')
print(type(n))
print(f'{n} é um número? ', n.isnumeric())
print(f'{n} é um texto? ', n.isalpha())
print(f'{n} é um texto com números? ', n.isalnum())
print(f'{n} é um texto com números? ', n.isalnum())