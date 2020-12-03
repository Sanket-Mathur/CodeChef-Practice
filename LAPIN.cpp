#include <bits/stdc++.h>
using namespace std;

void check(string s) {
    string L = s.substr(0, s.size()/2), R;
    if(s.size() % 2 == 0)
        R = s.substr(s.size()/2, s.size());
    else
        R = s.substr(s.size()/2 + 1, s.size());
    for(int i = 0; i < L.size(); i++) {
        bool found = false;
        for(int j = 0; j < L.size(); j++) {
            if(L[i] == R[j]) {
                R[j] = NULL;
                found = true;
                break;
            }
        }
        if(!found) {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
}

int main() {
	string str;
	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
	    cin >> str;
	    check(str);
	}
	return 0;
}

