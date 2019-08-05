#include <iostream>
using namespace std;

int vertificar(int vetor[], int qnt)
{
    if(qnt == 1)
        return 1;
    else if(qnt == 2)
    {
        if (vetor[0] !=  vetor[1])
            return 1;
        else
            return 0;
    }
    else
    {   
        bool maior = vetor[0] >  vetor[1];
        for(int i = 1; i < qnt - 1; i ++)
        {
            if(maior && vetor[i] >= vetor[i + 1])
                return 0;
            else if (!maior && vetor[i] <= vetor[i + 1])
                return 0;
            
            maior = !maior;
        }       
        return 1;
    }

}

int main()
{
    int qnt;
    cin >> qnt;
    int montanhas[qnt + 10];
    for(int i = 0; i < qnt; i ++)
        cin >> montanhas[i];
    
    cout << vertificar(montanhas, qnt) << endl;

    return 0;
}