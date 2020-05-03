from itertools import permutations


def main():
    
    n = int(input())
    
    for loop in range(n):
        entrada = input()
    
        for i in sorted(set(permutations(entrada)), key=lambda x: ''.join(x)):
            print(''.join(i))
        print()


if __name__ == '__main__':
    main()
