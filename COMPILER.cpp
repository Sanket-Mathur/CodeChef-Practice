#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; ++t) {
	    string S;
	    cin >> S;
	    long int stack = 0, len = 0;
	    for(int i = 0; i < S.size(); ++i) {
	        if (S[i] == '<') {
	            ++stack;
	        } else {
	            --stack;
	            if (stack < 0) {
	                break;
	            } else if (stack == 0) {
	                len = i+1;
	            }
	        }
	    }
	    cout << len << endl;
	}
	return 0;
}

