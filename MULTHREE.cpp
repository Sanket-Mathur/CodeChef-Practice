#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
	    long long int k, sum;
	    int d0, d1, s;
	    cin >> k >> d0 >> d1;
	    s = d0 + d1;
	    sum = s;
	    if(k == 3) {
	        sum += s % 10;
	    } else if(k > 3) {
	        sum += s % 10;
	        k -= 3;
	        for(int j = 0; j < k/4; j++) {
	            sum += (2*s)%10 + (4*s)%10 + (6*s)%10 + (8*s)%10;
	        }
	        if(k%4 >= 1)
	            sum += (2*s)%10;
	        if(k%4 >= 2)
	            sum += (4*s)%10;
	        if(k%4 >= 3)
	            sum += (8*s)%10;
	    }
	    if(sum % 3 == 0)
	        cout << "YES" << endl;
	    else
	        cout << "NO" << endl;
	}
	return 0;
}

