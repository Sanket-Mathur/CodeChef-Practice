#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
	    int activities;
	    string origin;
	    long long laddus = 0;
	    cin >> activities >> origin;
	    for(int a = 0; a < activities; a++) {
	        string act;
	        cin >> act;
	        if(act == "CONTEST_WON") {
	            int rank;
	            cin >> rank;
	            laddus += 300;
	            if(rank < 20) 
	                laddus += 20-rank;
	        } else if(act == "TOP_CONTRIBUTOR") {
	            laddus += 300;
	        } else if(act == "BUG_FOUND") {
	            int severity;
	            cin >> severity;
	            laddus += severity;
	        } else {
	            laddus += 50;
	        }
	    }
	    if(origin == "INDIAN")
	        cout << laddus / 200 << endl;
	    else
	        cout << laddus / 400 << endl;
	}
	return 0;
}

