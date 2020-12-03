#include <iostream>
using namespace std;

int main() {
    int t, no, rev, d;
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> no;
        rev = 0;
        while(no) {
            d = no % 10;
            rev = 10*rev + d;
            no /= 10;
        }
        cout << rev << endl;
    }
	return 0;
}

