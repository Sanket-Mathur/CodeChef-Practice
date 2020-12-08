#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main() {
	int T;
	lli N;
	cin >> T;
	for(int t = 0; t < T; t++) {
	    cin >> N;
	    vector<lli> S(N);
	    for(lli i = 0; i < N; i++)
	        cin >> S[i];
	    lli L = N, total = 0;
	    while(L > 0) {
	        lli min_index = 0;
	        for(lli i = 0; i < L; i++) {
	            if(S[i] < S[min_index]) {
	                min_index = i;
	            }
	        }
	        total += S[min_index] * L;
	        for(lli i = 0; i < L; i++)
	            S[i] -= S[min_index];
	        L = min_index;
	    }
	    cout << total << endl;
	}
	return 0;
}

