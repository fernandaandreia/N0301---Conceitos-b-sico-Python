# -*- coding: utf-8 -*_

# valor1 = float(input ("Digite um número aleatório: "))
# valor2 = float(input("Digite outro número aleatório: "))
# soma = valor1+valor2
# subtracao = valor1-valor2
# divisao = valor1/valor2
# resto_da_divisao = valor1%valor2
# media = valor1+valor2/2
# multiplicacao = valor1*valor2

# print(f' Os resultados foram: Soma {soma} | Subtracao: {subtracao} | Divisão: {divisao} | Resto da Divisão: {resto_da_divisao} | Média: {media} | Multiplicacao: {multiplicacao}')

# nome_do_usuario = input("Nome: ")
# idade_usuario = int(input("Idade: "))

# if idade_usuario >= 18:
#     print(f' Olá, {nome_do_usuario} , pode entrar')

# elif idade_usuario <=17 and idade_usuario >=11:
#     print(f'Você é menor de idade {nome_do_usuario}')

# else:
#     print(f'Vc é menor de idade {nome_do_usuario}, você ainda é crianca')

# lista1 = ['eu', 'to com sono', 'blz']

# for i in lista1:
# if i is 'eu':
#     print ('tá acabando a aula')
#     break
    
    
# print(i)

# print('--- while ---')

# number = 0

# while number <= 10 and number > 1:
#     print(number)
#     number = number+

import datetime

dia_de_nasc = datetime.date(1994, 1, 20)

def calcular_dias_de_vida(data):
    if data is None:
        error = 'ops'
        return error

    hoje = datetime.date.today()
    dias_de_vida = hoje - data
    return dias_de_vida
    

retorno = calcular_dias_de_vida(dia_de_nasc)
print(retorno)
