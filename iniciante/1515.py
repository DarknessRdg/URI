class Mensagem:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo
    
    def __str__(self):
        return self.nome


def main():
    qnt = int(input())
    while qnt != 0:
        vetor = []
        for i in range(qnt):
            planeta, ano, tempo = input().split()
            tempo = int(ano) - int(tempo)
            vetor.append(Mensagem(planeta, tempo))
        
        vetor.sort(key=lambda x: x.tempo)
        print(vetor[0])

        qnt = int(input())


if __name__ == "__main__":
    main()