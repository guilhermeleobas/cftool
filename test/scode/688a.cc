#include <iostream>
#include <string>

using namespace std;

int main (){

  int n, d;
  
  cin >> n >> d;
  
  int ans = -1;
  int cd = 0;
  for (int i=0; i<d; i++){
    int aux = 0;
    string s;
    cin >> s;
    
    for (int j=0; j<s.size(); j++){
      if ( s[j] == '1' )
        aux += 1;
    }
    if (aux != n){
      cd += 1;
      ans = max(ans, cd);
    }
    else{
      ans = max(ans, cd);
      cd = 0;
    }
  }
  cout << ans << endl;
  return 0;
}
