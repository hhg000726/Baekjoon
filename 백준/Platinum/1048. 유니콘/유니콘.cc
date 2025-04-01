#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

const long long mod = 1000000007;
int N, M, L;
vector<vector<long long>> dp;
vector<string> maps;
string s;

unordered_map<char, vector<pair<int, int>>> where;

vector<vector<long long>> build_prefix(const vector<vector<long long>>& dp) {
  vector<vector<long long>> P(N + 1, vector<long long>(M + 1, 0));
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      P[i + 1][j + 1] = (dp[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j] + mod) % mod;
  return P;
}

long long rect_sum(const vector<vector<long long>>& P, int r1, int c1, int r2, int c2) {
  r1 = max(r1, 0);
  c1 = max(c1, 0);
  r2 = min(r2, N-1);
  c2 = min(c2, M-1);
  if (r1 > r2 || c1 > c2) return 0;
  return (P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1] + mod) % mod;
}

int main(void)
{
  cin >> N >> M >> L;
  cin >> s;
  maps.resize(N);
  dp.resize(N);
  for (int i = 0; i < N; i++) {
    string t;
    cin >> t;
    maps[i] = t;
    for (int j = 0; j < M; j++) {
      where[maps[i][j]].push_back({i, j});
      dp[i].push_back(0);
    }
  }

  for (auto& [i, j] : where[s[0]]) {
    dp[i][j] = 1;
  }
    
  for (int index = 1; index < s.length(); index++) {
    vector<vector<long long>> P = build_prefix(dp);
    vector<vector<long long>> new_dp(N, vector<long long>(M, 0));
    for (auto& [nx, ny] : where[s[index]]) {
      long long sumA = (
        rect_sum(P, 0, 0, nx-3, ny-2) +
        rect_sum(P, 0, ny+2, nx-3, M-1) +
        rect_sum(P, nx+3, 0, N-1, ny-2) +
        rect_sum(P, nx+3, ny+2, N-1, M-1) +
        mod
      ) % mod;
      long long sumB = (
        rect_sum(P, 0, 0, nx-2, ny-3) +
        rect_sum(P, 0, ny+3, nx-2, M-1) +
        rect_sum(P, nx+2, 0, N-1, ny-3) +
        rect_sum(P, nx+2, ny+3, N-1, M-1) +
        mod
      ) % mod;
      long long sumAB = (
        rect_sum(P, 0, 0, nx-3, ny-3) +
        rect_sum(P, 0, ny+3, nx-3, M-1) +
        rect_sum(P, nx+3, 0, N-1, ny-3) +
        rect_sum(P, nx+3, ny+3, N-1, M-1) +
        mod
      ) % mod;
      new_dp[nx][ny] = (sumA + sumB - sumAB + mod) % mod;
    }
    dp = new_dp;
  }

  long long result = 0;

  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      result = (result + dp[i][j]) % mod;
  
  cout << result;

  return 0;
}