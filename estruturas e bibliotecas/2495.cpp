#include<bits/stdc++.h>
using namespace std;


int main()
{
    int qnt;
     while(cin >> qnt){
        int sum = 0, entrada = 0;

		for (int i = 0; i < qnt - 1; i ++) {
			cin >> entrada;
			sum += entrada;
		}
		
		int sum_pa = (int) (1 + qnt) * qnt / 2;
		
		cout << sum_pa - sum << endl;	
     }
    return 0;
}