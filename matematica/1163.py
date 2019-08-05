import math
def main():
    while True:
        g = 9.80665
        try:
            h_zinho = float(input())
            p1, p2 = map(int, input().split())
            for i in range(int(input())):    
                angulo, velocidade = map(float, input().split())

                angulo = convert(angulo)
                seno = math.sin(angulo)
                coss = math.cos(angulo)

                vy = velocidade * seno
                vx = velocidade * coss

                t_subida = vy / g
                H = vy * t_subida + (- g * (t_subida ** 2)) / 2 + h_zinho
                
                tempo  = t_subida + ((2 * H / g) ** (1/2))
                distancia = vx * tempo

                if p1 <= distancia <= p2:
                    print('{:.5f} -> DUCK'.format(distancia))
                else:
                    print('{:.5f} -> NUCK'.format(distancia))
        except EOFError:
            break

def convert(n):
    return 3.14159 * n / 180


if __name__ == "__main__":
    main()