text = str(input('Text: '))

letter = 0  
word = 1
setence = 0

tam = len(text)

for i in range(tam):

    if text[i] >= 'A' and text[i] <= 'Z' or text[i] >= 'a' and text[i] <= 'z':
        letter = letter + 1
        
    elif text[i] == ' ':
        word = word + 1
        
    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        setence = setence + 1
        
L = letter / word * 100
S = setence / word * 100

index = (0.0588 * L) - (0.296 * S) - 15.8
index = round(index)

if index > 16:    
        print('Grade 16+\n')
    
elif index < 1:
    print('Before Grade 1\n')
    
else:    
    print('Grade', index)
