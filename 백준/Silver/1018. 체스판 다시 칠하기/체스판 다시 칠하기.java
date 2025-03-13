import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] input = br.readLine().split(" ");
    int N = Integer.parseInt(input[0]);
    int M = Integer.parseInt(input[1]);
    char[][] board = new char[N][M];
    for (int i = 0; i < N; i++)
      board[i] = br.readLine().toCharArray();
    char[] color = {'W', 'B'};
    int[][] cost1 = new int[N][M];
    int[][] cost2 = new int[N][M];
    int[][] prefix1 = new int[N + 1][M + 1];
    int[][] prefix2 = new int[N + 1][M + 1];
    int answer = 2500;
    for (int i = 0; i < N + 1; i++) {
      for (int j = 0; j < M + 1; j++) {
        prefix1[i][j] = 0;
        prefix2[i][j] = 0;
      }
    }
    for (int i = 0; i < N; i++) {
      char b = color[i % 2];
      for (int j = 0; j < M; j++) {
        if (board[i][j] != b) cost1[i][j] = 1;
        else cost1[i][j] = 0;
        if (b == 'W') b = 'B';
        else b = 'W';
      }
    }
    for (int i = 1; i < N + 1; i++)
      for (int j = 1; j < M + 1; j++)
        prefix1[i][j] = cost1[i - 1][j - 1] + prefix1[i][j - 1] + prefix1[i - 1][j] - prefix1[i - 1][j - 1];
    for (int i = 0; i < N; i++) {
      char b = color[(i + 1) % 2];
      for (int j = 0; j < M; j++) {
        if (board[i][j] != b) cost2[i][j] = 1;
        else cost2[i][j] = 0;
        if (b == 'W') b = 'B';
        else b = 'W';
      }
    }
    for (int i = 1; i < N + 1; i++)
      for (int j = 1; j < M + 1; j++)
        prefix2[i][j] = cost2[i - 1][j - 1] + prefix2[i][j - 1] + prefix2[i - 1][j] - prefix2[i - 1][j - 1];
    for (int i = 8; i < N + 1; i++) {
      for (int j = 8; j < M + 1; j++) {
        answer = Math.min(answer, prefix1[i][j] - prefix1[i - 8][j] - prefix1[i][j - 8] + prefix1[i - 8][j- 8]);
        answer = Math.min(answer, prefix2[i][j] - prefix2[i - 8][j] - prefix2[i][j - 8] + prefix2[i - 8][j- 8]);
      }
    }
    System.out.println(answer);
  }
}