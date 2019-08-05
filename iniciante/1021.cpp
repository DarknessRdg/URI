#include <iostream>
#include <math.h>
using namespace std;


int main(){
	float moeda_double;
	int moeda, qnt;
	cin >> moeda_double;
	
	moeda = trunc(moeda_double);
	cout << "NOTAS:" << endl;
   	qnt = (int) moeda / 100;
	cout << qnt << " nota(s) de R$ 100.00" << endl;
	moeda -= qnt * 100;
	
	qnt = (int) moeda / 50;
	cout << qnt << " nota(s) de R$ 50.00" << endl;
	moeda -= qnt * 50;
	
	qnt = (int) moeda / 20;
	cout << qnt << " nota(s) de R$ 20.00" << endl; 
	moeda -= qnt * 20;
	
	
	qnt = (int) moeda / 10;
	cout << qnt << " nota(s) de R$ 10.00" << endl; 
	moeda -= qnt * 10;
	
	qnt = (int) moeda / 5;
	cout << qnt << " nota(s) de R$ 5.00" << endl; 
	moeda -= qnt * 5;
	
	qnt = (int) moeda / 2;
	cout << qnt << " nota(s) de R$ 2.00" << endl; 
	moeda -= qnt * 2;

	
	/*--------------------------------------------------*/
	double temp;
	int decimal = round(modf(moeda_double, &temp) * 100);
	
	moeda = moeda * 100 + decimal;
	cout << "MOEDAS:" << endl;
	
	qnt = (int) moeda / 100;
	cout << qnt << " moeda(s) de R$ 1.00" << endl;
	moeda -= qnt * 100;
	
	qnt = (int) moeda / 50;
	cout << qnt << " moeda(s) de R$ 0.50" << endl;
	moeda -= qnt * 50;
	
	qnt = (int) moeda / 25;
	cout << qnt << " moeda(s) de R$ 0.25" << endl;
	moeda -= qnt * 25; 
	
	qnt = (int) moeda / 10;
	cout << qnt << " moeda(s) de R$ 0.10" << endl;
	moeda -= qnt * 10;
	
	qnt = (int) moeda / 5;
	cout << qnt << " moeda(s) de R$ 0.05" << endl;
	moeda -= qnt * 5;
	
	cout << moeda << " moeda(s) de R$ 0.01" << endl;
	return 0;
}	