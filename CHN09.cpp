#include <iostream>
#include <cstring>

using namespace std;

int main() {
	
	int n;
	cin >> n;
	for(int t = 0; t < n; t++) {
	    char s[100];
	    cin >> s;
	
	    int a = 0, b = 0;
	    for(int i = 0; i < strlen(s); i++) {
	        if(s[i] == 'a')
	            a++;
	        else
	            b++;
	    }
	
	    int min = a<=b?a:b;
	    cout << min << endl;
	}
	
	return 0;
}
