def main():
    n = int(input())

    p = input()
    ordenada = sorted(p)

    cont = 0
    for i in range(n):
        if p[i] != ordenada[i]:
            cont += 1


    if cont != 2:
        print("There aren't the chance.")
    else:
        print("There are the chance.")


if __name__ == '__main__':
    for i in range(int(input())):
        main()
  
