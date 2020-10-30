''' Pegando input do usuário '''
num1 = float(input('Digite um número:'))
op = str(input('Digite a operação: '))
num2 = float(input('Digite outro número:'))
res = 0

cont = True

''' Função para calcular de acordo com input do usuário '''
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

''' Imprimindo resultado obtido '''
res = calcular(num1, num2)
print('O resultado é: ', res)

''' Looping de repetição do código ate o usuário dizer que não deseja continuar '''
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
        
