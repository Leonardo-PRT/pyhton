''' Pegando o inút do usuário '''
text = str(input('Text: '))

''' Declarando variáveis '''
letter = 0  
word = 1
setence = 0
tam = len(text)

''' Percorrendo o texto do usuário '''
for i in range(tam):
    
    ''' Contagem de números de frases, letras e palavras '''
    if text[i] >= 'A' and text[i] <= 'Z' or text[i] >= 'a' and text[i] <= 'z':
        letter = letter + 1
        
    elif text[i] == ' ':
        word = word + 1
        
    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        setence = setence + 1

''' Contagem do nível de dificuldade de leitura '''       
L = letter / word * 100
S = setence / word * 100

index = (0.0588 * L) - (0.296 * S) - 15.8
index = round(index)

''' Printando o graú de ligibilidade '''
if index > 16:    
        print('Grade 16+\n')
    
elif index < 1:
    print('Before Grade 1\n')
    
else:    
    print('Grade', index)
