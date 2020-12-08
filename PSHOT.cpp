#include <bits/stdc++.h>
using namespace std;

int main() {
	string S;
	int T, N;
	cin >> T;
	for(int t = 0; t < T; t++) {
	    cin >> N;
	    cin >> S;
	    int score1 = 0, score2 = 0, attempt1 = 0, attempt2 = 0;
	    bool flag = true;
	    for(int i = 0; i < 2*N; i++) {
	        if(i%2==0)
	            attempt1++;
	        else
	            attempt2++;
	        if(S[i] == '1')
	            if(i%2==0)
	                score1++;
	            else
	                score2++;
	        if(score1-score2 > N-attempt2 || score2-score1 > N-attempt1) {
	            cout << i+1 << endl;
	            flag = false;
	            break;
	        }
	    }
	    if(flag)
	        cout << 2*N << endl;
	}
	return 0;
}

