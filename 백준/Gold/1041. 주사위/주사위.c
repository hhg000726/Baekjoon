#include <stdio.h>

int main() {
  long long sum = 0, n, dice[6], max1 = 0, min1 = 50, min2 = 100, min3 = 150;
  scanf("%lld", &n);
  for (int i = 0; i < 6; i++) {
    scanf("%lld", &dice[i]);
    if (dice[i] < min1)
      min1 = dice[i];
    if (dice[i] > max1)
      max1 = dice[i];
  }
  int combinations[8][3] = {
    {0, 1, 2}, {0, 1, 3}, {0, 2, 4}, {0, 3, 4},
    {5, 1, 2}, {5, 1, 3}, {5, 2, 4}, {5, 3, 4}
  };
  for (int i = 0; i < 8; i++) {
    long long tsum = dice[combinations[i][0]] + dice[combinations[i][1]] + dice[combinations[i][2]];
    if (tsum < min3) {
        min3 = tsum;
    }
  }
  int combinations2[12][2] = {
    {0, 1}, {0, 2}, {0, 3}, {0, 4},
    {5, 1}, {5, 2}, {5, 3}, {5, 4},
    {1, 2}, {1, 3}, {2, 4}, {3, 4}
  };
  for (int i = 0; i < 12; i++) {
    long long tsum = dice[combinations2[i][0]] + dice[combinations2[i][1]];
    if (tsum < min2) {
        min2 = tsum;
    }
  }
  if (n == 1) {
    for (int i = 0; i < 6; i++)
      sum += dice[i];
    sum -= max1;
  }
  else {
    sum += (n * n - 3 * n + 2) * min1 * 4 + (n - 2) * (n - 2) * min1 + ((n - 2) * 4 + (n - 1) * 4) * min2 + 4 * min3;
  }
  printf("%lld", sum);
}