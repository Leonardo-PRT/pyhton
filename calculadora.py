
num1 = float(input('Digite um número:'))
op = str(input('Digite a operação: '))
num2 = float(input('Digite outro número:'))
res = 0

cont = True

def calcular(num1, num2):

    if op == '+':
        return num1 + num2
        
    elif op == '-':
        return num1 - num2

    elif op == '/':
        return num1 / num2

    elif op == '*':
        return num1 * num2

    elif op == '**':
        return num1 ** num2

res = calcular(num1, num2)
print('O resultado é: ', res)

while cont :
    
    continuar = str(input('Deseja continuar? (s/n) '))

    if continuar != 's':
        cont = False
        print('O resultado final é: ', res)
        break

    else:
        op = str(input('Digite a operação: '))
        num2 = int(input('Digite outro número:'))
        res = calcular(res, num2)
        print('Resultado é: ', res)
        
