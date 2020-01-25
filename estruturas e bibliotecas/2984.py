entrada = list(input())

pilha = []

for i in entrada:
    if i == ')':
        if pilha:
            pilha.pop()
    else:
        pilha.append(')')


if pilha:
    print('Ainda temos {} assunto(s) pendente(s)!'.format(len(pilha)))
else:
    print('Partiu RU!')
    
