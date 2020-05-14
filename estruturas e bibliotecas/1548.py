for i in range(int(input())):
    input()
    alunos = list(map(int, input().split()))
    ord = sorted(alunos, reverse=True)
    
    cont = 0
    for i in range(len(alunos)):
        if alunos[i] == ord[i]:
            cont += 1
    print(cont)
