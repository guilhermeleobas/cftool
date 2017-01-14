#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main (){

	int n;
	cin >> n;

	vector<int> v (n);

	vector<pair<int, int> > pairs;
	vector<int> soma;

	int aux = 0;
	for (int i=0; i<n; i++){
		cin >> v[i];
		aux += v[i];
	}


	if (aux != 0){
		cout << "YES\n1\n1 " << n << "\n";
		return 0;
	}
	else{
		aux = 0;
		for (int i=0; i<n; i++){
			aux += v[i];
			if (aux != 0){
				cout << "YES\n";
				cout << "2\n";
				cout << "1 " << i+1 << endl;
				cout << i+2 << ' ' << n << endl;
				return 0;
			}
		}
	}

	cout << "NO" << endl;

	return 0;
}
