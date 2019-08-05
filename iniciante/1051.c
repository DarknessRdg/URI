#include <stdio.h>

void main(){
    float salario, imposto;

    scanf("%f", &salario);
    if (salario <= 2000.00){
        printf("Isento\n");
    }else if (salario <= 3000){
        imposto = (salario - 2000) * 0.08;
    }else if (salario <= 4500){
        imposto = (salario - 2000 - 1000) * 0.18 + 80;
    }else{
        imposto = (salario - 2000 - 1000 - 1500) * 0.28 + 80 + (1500 * 0.18);
    }

    if (salario > 2000){
        printf("R$ %.2f\n", imposto);
    }
}
