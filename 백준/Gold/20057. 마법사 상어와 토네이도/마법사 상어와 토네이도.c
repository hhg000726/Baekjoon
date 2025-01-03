#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
  char input[3000];
  int N, answer = 0, direction = 3;
  fgets(input, sizeof(input), stdin);
  N = atoi(input);
  int sand[N][N], x = (N - 1) / 2, y = (N - 1) / 2;
  bool visited[N][N];

  for (int i = 0; i < N; i++) {
    fgets(input, sizeof(input), stdin);
    char *ptr = input;
    for (int j = 0; j < N; j++) {
      sand[i][j] = strtol(ptr, &ptr, 10);
      visited[i][j] = false;
    }
  }

  int directions[4][2] = {
    {0, -1}, {1, 0}, {0, 1}, {-1, 0}
  };

  int rests[4][9][3] = {
    {{-2, 0, 2}, {-1, -1, 10}, {-1, 0, 7}, {-1, 1, 1}, {0, -2, 5}, {1, -1, 10}, {1, 0, 7}, {1, 1, 1}, {2, 0, 2}}, 
    {{0, -2, 2}, {1, -1, 10}, {0, -1, 7}, {-1, -1, 1}, {2, 0, 5}, {1, 1, 10}, {0, 1, 7}, {-1, 1, 1}, {0, 2, 2}}, 
    {{-2, 0, 2}, {-1, 1, 10}, {-1, 0, 7}, {-1, -1, 1}, {0, 2, 5}, {1, 1, 10}, {1, 0, 7}, {1, -1, 1}, {2, 0, 2}}, 
    {{0, -2, 2}, {-1, -1, 10}, {0, -1, 7}, {1, -1, 1}, {-2, 0, 5}, {-1, 1, 10}, {0, 1, 7}, {1, 1, 1}, {0, 2, 2}}
  };

  visited[x][y] = true;

  while (true) {
    if (visited[x + directions[(direction + 1) % 4][0]][y + directions[(direction + 1) % 4][1]] == false) {
      direction = (direction + 1) % 4;
    }
    x += directions[direction][0];
    y += directions[direction][1];
    visited[x][y] = true;

    int s = 0;
    for (int i = 0; i < 9; i++) {
      int dx = x + rests[direction][i][0];
      int dy = y + rests[direction][i][1];
      int t = sand[x][y] * rests[direction][i][2] / 100;
      s += t;
      if (dx > -1 && dx < N && dy > -1 && dy < N) {
        sand[dx][dy] += t;
      }
      else {
        answer += t;
      }
    }

    sand[x][y] -= s;

    if (x + directions[direction][0] == -1 || x + directions[direction][0] == N || y + directions[direction][1] == -1 || y + directions[direction][1] == N) {
      answer += sand[x][y];
    }
    else {
      sand[x + directions[direction][0]][y + directions[direction][1]] += sand[x][y];
    }
    sand[x][y] = 0;

    if (x == 0 && y == 0) break;
  }

  printf("%d", answer);
}