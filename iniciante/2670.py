def main():
    a = int(input())
    b = int(input())
    c = int(input())

    tempos = []

    t1 = b * 2 + c * 4
    tempos += [t1]
    
    t2 = a * 2 + c * 2
    tempos += [t2]
    
    t3 = a * 4 + b * 2
    tempos += [t3]

    menor = t1
    for i in range(1, len(tempos)):
        if tempos[i] < menor:
            menor = tempos[i]

    print(menor)


if __name__ == '__main__':
    main()