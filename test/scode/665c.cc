#include <iostream>
#include <string>

using namespace std;

char get(const string& s, const int pos)
{
  for (char c = 'a'; c < 'z'; c++) {
    if (pos == 0) {
      if (c != s[pos + 1])
        return c;
    } else {
      if (c != s[pos + 1] and c != s[pos - 1])
        return c;
    }
  }
}

int main()
{

  string s;

  cin >> s;
  for (int i = 0; i < s.size(); i++) {

    int j = i;
    while (j < s.size() and s[i] == s[j]){
      j++;
    }
    
    if (s[i] != s[j] and j - i <= 1)
      continue;

    char c = 'a';

    while (c == s[i] or (i > 0 and c == s[i - 1]) or (j < s.size() and c == s[j]))
      c++;

    for (int k = i+1; k < j; k += 2) {
      s[k] = c;
    }

    i = j-1;
  }

  cout << s << endl;

  return 0;
}
