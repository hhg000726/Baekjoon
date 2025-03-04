#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

vector<vector<long long>> decreasing = {{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {}, {}, {}, {}, {}, {}, {}, {}, {}};

void func(int i) {
    long long power1 = 1, power2 = 10;
    for (int p = 1; p < i; p++) {
        power1 *= 10;
        power2 *= 10;
    }
    for (int j = 0; j < decreasing[i - 1].size(); j++) {
        for (int k = decreasing[i - 1][j] / power1 + 1; k < 10; k++) {
            decreasing[i].push_back(k * power2 + decreasing[i - 1][j]);
        }
    }
}

int main() {
    int N;
    cin >> N;
    for (int i = 1; i < 10; i++) {
        func(i);
    }
    vector<long long> ans;
    for(const auto& v : decreasing) {
        ans.insert(ans.end(), v.begin(), v.end());
    }
    sort(ans.begin(), ans.end());
    if (N >= ans.size()) {
        cout << -1 << endl;
    } else {
        cout << ans[N] << endl;
    }
}
