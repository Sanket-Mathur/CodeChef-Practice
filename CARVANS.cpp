#include <iostream>
using namespace std;

int main() {
	int t, n;
	cin >> t;
	for(int i = 0; i < t; i++) {
	    cin >> n;
	    long long current, pre = INT32_MAX;
	    int count = 0;
	    for(int j = 0; j < n; j++) {
	        cin >> current;
	        if(current <= pre) {
	            pre = current;
	            count++;
	        }
	    }
	    cout << count << endl;
	}
	return 0;
}

