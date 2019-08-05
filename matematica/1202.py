from math import sqrt
def main():
    n = int(input())
    for i in range(n):
        binario = input()
        normal = int(binario, 2)
        
        s = fib(normal % 1500)
        if s > 999:
                s = str(s)
                tam = len(s)
                print('{}'.format(s[tam-3:]))
        else:
                print('{0:3}'.format(s).replace(' ', '0'))
        

def pisano_length(m):
    i = 2
    while fib(i) % m != 0:
        i += 1
    if fib(i+1) % m != 1:
        while fib(i+1) % m != 1:
            i += i
    return(i)


def fib(n):
    a, b = 0, 1
    if(n == 0 or n == 1):
        return n
    else:
        for i in range(2,n+1):
            b, a = a + b, b
    return b


if __name__ == '__main__':
	main()