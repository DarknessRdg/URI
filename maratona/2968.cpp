#include <iostream>
#include <math.h>
using namespace std;


int main() {
	int v, n;
	cin >> v >> n;
	
	int total = v * n;
	
	for (int i = 1; i <= 9; i += 1) {
		double qnt = total * (i / 10.0);
		
		
		if (qnt - (trunc(qnt)) != 0.0)
			cout <<  (int)qnt + 1;
		else 	
			cout << (int)qnt;
		
		if (i != 9)
			cout << " ";
	}
	cout << endl;
	return 0;
}