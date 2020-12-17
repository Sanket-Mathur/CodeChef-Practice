#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, I;
	cin >> N;
	stack<int> s;
	int count=0, depth=1, depth_index=1, counter=0, length=0, temp_counter=0, temp_index, length_index;
	for (int i = 0; i < N; ++i) {
	    cin >> I;
	    if (I == 1) {
	        ++count;
	        if (s.empty())
	            temp_index = i+1;
	        ++temp_counter;
	        s.push(I);
	    } else {
	        if (count > depth) {
	            depth = count;
	            depth_index = i;
	        }
	        --count;
	        ++temp_counter;
	        s.pop();
	        if (s.empty()) {
	            if (temp_counter > length) {
	                length = temp_counter;
	                length_index = temp_index;
	            }
	            temp_counter = 0;
	        }
	    }
	}
	cout << depth << ' ' << depth_index << ' ' << length << ' ' << length_index << endl;
	return 0;
}

