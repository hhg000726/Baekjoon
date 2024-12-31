#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

int main() {
  int N, sum = 0, count = 0, treesum = 0;

  cin >> N;

  vector<tuple<int, int, int>> q = {};
  bool taken[N] = {false};
  int tree[N] = {-1};

  for (int i = 0; i < N; i++) {
    string input;
    cin >> input;
    int j = 0;
    tree[i] = i;
    for (char ch : input) {
      int len = ch == '0' ? 0 : (ch < 97 ? ch - 38: ch - 96);
      q.emplace_back(len, i, j);
      sum += len;
      j += 1;
    }
  }

  sort(q.begin(), q.end());

  for (tuple<int, int, int> t : q) {
    int len, i, j;
    tie(len, i, j) = t;
    if (i != j && len != 0 && tree[i] != tree[j]) {
      taken[i] = true;
      taken[j] = true;
      count += 1;
      int treej = tree[j];
      for (int k = 0; k < N; k++)
        if (tree[k] == treej)
          tree[k] = tree[i];
      treesum += len;
    }
  }
  
  if (count == N - 1)
    cout << sum - treesum;
  else
    cout << -1;
  
  return 0;
}