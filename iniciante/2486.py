def main():
    contadores = {'s': 0, 'b': 0, 'a': 0, 's_s': 0, 'b_s': 0, 'a_s': 0}
    qnt = int(input())
    for i in range(qnt):
        input()  # nome
        s, b, a = map(int, input().split())
        
        contadores['s'] += s
        contadores['b'] += b
        contadores['a'] += a

        s, b, a = map(int, input().split())
        contadores['s_s'] += s
        contadores['b_s'] += b
        contadores['a_s'] += a

    print('Pontos de Saque: {:.2f} %.'.format(contadores['s_s'] / contadores['s'] * 100))
    print('Pontos de Bloqueio: {:.2f} %.'.format(contadores['b_s'] / contadores['b'] * 100))
    print('Pontos de Ataque: {:.2f} %.'.format(contadores['a_s'] / contadores['a'] * 100))
    
if __name__ == "__main__":
    main()