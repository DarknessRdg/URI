class Pessoa:
    def __init__(self, nome, distancia, zona):
        self.nome = nome.capitalize()
        self.distancia = float(distancia)
        self.zona = zona.lower()

    def __str__(self):
        return self.nome


def main():
    while True:
        try:
            x = int(input())
            lista = []
            for i in range(x):
                nome, zona, distancia = input().split()
                lista.append(Pessoa(nome, distancia, zona))
            
            for i in sorted(lista, key=lambda x: (x.distancia, x.zona, x.nome)):
                print(i)
        except:
            break

            
if __name__ == "__main__":
    main()