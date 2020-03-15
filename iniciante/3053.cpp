#include <iostream>
#define optimize ios::sync_with_stdio(false);cin.tie(NULL)
using namespace std;

int main() {
	int qnt, i;
	char copo;
	int movimento;
	
	cin >> 	qnt;
	cin >> copo;
	
	for (i = 0; i < qnt; i++) {
		cin >> movimento;
		
		switch(movimento)
		{
		case 1:
			if(copo == 'A')
				copo = 'B';
			else if (copo == 'B')
				copo = 'A';
			break;
		case 2:
			if(copo == 'B')
				copo = 'C'; 
			else if (copo == 'C')
				copo = 'B';
			break;
		case 3:
			if(copo == 'A')
				copo = 'C'; 
			else if (copo == 'C')
				copo = 'A';
			break;
		}
	}
	
	cout << copo << endl;
	return 0;
}
