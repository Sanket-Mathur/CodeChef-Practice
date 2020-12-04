#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ll t, n;
	cin >> t;
	for(ll i = 0; i < t; i++) {
	    cin >> n;
	    ll n5 = 0;
	    while(n != 0) {
	        n /= 5;
	        n5 += n;
	    }
	    cout << n5 << endl;
	}
	return 0;
}

