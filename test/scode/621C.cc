#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

#define endl '\n'

int main (){
  int n, p;
  double sharks[100000 + 1000];
  
  cin >> n >> p;
  
  for (int i=0; i<n; i++){
    int l, r;
    cin >> l >> r;
    
    int ll = (l/p)*p < l ? (l/p)*p + p : (l/p)*p;
    int rr = (r/p)*p;
    
    if (rr <= r and ll >= l){
      int cnt = (rr-ll)/p + 1;
      sharks[i] = (double)(cnt)/(r-l+1);
    }
    else {
      sharks[i] = 0.0;
    }
  }
  
  double ans = 0.0;
  
  for (int i=0; i<n; i++){
    double c1 = sharks[i];
    double c2 = sharks[(i+1)%n];
    
    double prob = (1.0-c1)*c2 + (1.0-c2)*c1 + c1*c2;
    
    ans += prob*1000;  
  }
  
  cout << fixed << setprecision (6) << ans*2 << endl;
  
  return 0;
}
