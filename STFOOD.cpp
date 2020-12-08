#include <bits/stdc++.h>
using namespace std;

int main() {
	int T, N, S, V, P;
	cin >> T;
	for(int t = 0; t < T; t++) {
	    cin >> N;
	    int profit= INT_MIN;
	    for(int i = 0; i < N; i++) {
	        cin >> S >> P >> V;
	        profit = max(profit, V * (P / (S+1)));
	    }
	    cout << profit << endl;
	}
	return 0;
}

