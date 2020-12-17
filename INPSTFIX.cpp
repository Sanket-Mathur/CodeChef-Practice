#include <bits/stdc++.h>
using namespace std;

int priority(char c) {
    if (c == '^')
        return 3;
    else if (c == '*' || c == '/')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    return 0;
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
	    int N;
	    cin >> N;
	    string S;
	    cin >> S;
	    stack<char> Oper;
	    for (int i = 0; i < S.size(); ++i) {
	        if (isalpha(S[i])) {
	            cout << S[i];
	        } else if (S[i] == '(') {
	            Oper.push(S[i]);
	        } else if (S[i] == ')') {
	            while (Oper.top() != '(') {
	                cout << Oper.top();
	                Oper.pop();
	            }
	            Oper.pop();
	        } else {
	            while(!Oper.empty() && priority(Oper.top()) >= priority(S[i])) {
	                cout << Oper.top();
	                Oper.pop();
	            }
	            Oper.push(S[i]);
	        }
	    }
	    while (!Oper.empty()) {
	        cout << Oper.top();
	        Oper.pop();
	    }
	    cout << endl;
	}
	return 0;
}

