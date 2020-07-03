import os

num1 = int(input('digite um numero: '))
op = str(input('digite a operação: '))
num2 = int(input('digite outro numero: '))

if op == '+':
    resul = num1 + num2
    print(resul)

if op == '-':
    resul = num1 - num2
    print(resul)

if op == '*':
    resul = num1 * num2
    print(resul)

if op == '/':
    resul = num1 / num2
    print(resul)

if op == '**':
    resul = num1 ** num2
    print(resul)

cont = str(input('aperte "s" para continuar a operação, ou qualquer outra coisa para sair: '))

if cont != 's':
    print("resultado obtido: ", resul)

while cont == 's':
    op2 = str(input('digite a operação: '))
    num3 = int(input('digite um numero: '))
    
    
    if op2 == '+':
        resul = resul + num3
        print(resul)

    if op2 == '-':
        resul = resul - num3
        print(resul)

    if op2 == '*':
        resul = resul * num3
        print(resul)

    if op2 == '/':
        resul = resul / num3
        print(resul)

    if op2 == '**':
        resul = resul ** num3
        print(resul)

    
    cont = str(input('aperte "s" para continuar a operação, ou qualquer outra coisa para parar: '))

    if cont != 's':
        print('resultado obtido:', resul)
        break

    




    