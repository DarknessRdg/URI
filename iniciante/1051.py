def main():
    salario = float(input())
    if (salario <= 2000.00):
        print("Isento")
    elif (salario <= 3000):
        imposto = (salario - 2000) * 0.08
    elif (salario <= 4500):
        imposto = (salario - 2000 - 1000) * 0.18 + 80
    else:
        imposto = (salario - 2000 - 1000 - 1500) * 0.28 + 80 + (1500 * 0.18)

    if (salario > 2000):
        print("R$ %.2f" %imposto)


if __name__ == "__main__":
    main()
