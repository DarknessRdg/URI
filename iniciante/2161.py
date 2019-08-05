divisao = 1 / 6 
def main():
    x = int(input())
    print('{:.10f}'.format(3 + calc(x)))


def calc(n):
    if n == 0:
        return 0
    elif n == 1:
        global divisao
        return divisao 
    else:
        return 1 / (6 + calc(n - 1))
    

if __name__ == "__main__":
    main()