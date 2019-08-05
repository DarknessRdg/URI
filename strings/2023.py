def main():
    lista = []
    while True:
        try:
            ent = input()
            lista.append(ent)
        except:
            lista.sort(key=lambda i: i.upper())
            print(lista[len(lista) - 1])
            break



if __name__ == "__main__":
    main()