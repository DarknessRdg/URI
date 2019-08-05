def main():
    # minha primeira solucao
    salario = float(input())

    if salario <= 400:
        novo_salario = salario * 0.15 + (salario)
        reajuste_ganho =  novo_salario - salario
        print ('Novo salario: %.2f' %novo_salario)
        print('Reajuste ganho: %.2f' %reajuste_ganho)
        print('Em percentual: 15 %')
    elif 400.01 <= salario <= 800:
        novo_salario = salario * 0.12 + (salario)
        reajuste_ganho =  novo_salario - salario
        print ('Novo salario: %.2f' %novo_salario)
        print('Reajuste ganho: %.2f' %reajuste_ganho)
        print('Em percentual: 12 %')
    elif 800.01 <= salario <= 1200:
        novo_salario = salario * 0.1 + (salario)
        reajuste_ganho =  novo_salario - salario
        print ('Novo salario: %.2f' %novo_salario)
        print('Reajuste ganho: %.2f' %reajuste_ganho)
        print('Em percentual: 10 %')
    elif 1200.01 <= salario <= 2000:
        novo_salario = salario * 0.07 + (salario)
        reajuste_ganho =  novo_salario - salario
        print ('Novo salario: %.2f' %novo_salario)
        print('Reajuste ganho: %.2f' %reajuste_ganho)
        print('Em percentual: 7 %')
    else:
        novo_salario = salario * 0.04 + (salario)
        reajuste_ganho =  novo_salario - salario
        print ('Novo salario: %.2f' %novo_salario)
        print('Reajuste ganho: %.2f' %reajuste_ganho)
        print('Em percentual: 4 %')


def main2():
    # minha segunda solucao
    salario = float(input())
   
    if salario <= 400:
        reajuste = 0.15
    elif salario <= 800:
        reajuste = 0.12
    elif salario <= 1200:
        reajuste = 0.1
    elif salario <= 2000:
        reajuste = 0.07
    else: 
        reajuste =  0.04

    novo_salario = salario * reajuste + (salario)
    reajuste_salarial = novo_salario - salario
    porcentagem = reajuste * 100
    print ('Novo salario: %.2f' %novo_salario)
    print('Reajuste ganho: %.2f' %reajuste_salarial)
    print('Em percentual: %.f %%' %porcentagem)

if __name__ == "__main__":
    main()