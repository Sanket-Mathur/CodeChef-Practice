#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;
    vector<int> prices(n);
    for(int i = 0; i < n; i++)
        cin >> prices[i];
    sort(prices.begin(), prices.end());
    long long maximum = 0;
    for(int i = 0; i < n; i++)
        maximum = max(maximum, (long long)prices[i]*(n-i));
    cout << maximum << endl;
	return 0;
}
