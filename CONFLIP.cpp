#include <iostream>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> n;
        for(int j = 0; j < n; j++) {
            long long int N;
            int I, Q;
            cin >> I >> N >> Q;
            if(N % 2 == 0)
                cout << N / 2 << endl;
            else
                if(Q == I)
                    cout << N / 2 << endl;
                else
                    cout << N / 2 + 1 << endl;
        }
    }
	return 0;
}

