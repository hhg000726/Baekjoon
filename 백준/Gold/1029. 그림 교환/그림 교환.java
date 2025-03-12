import java.io.*;
import java.util.*;
public class Main {
  static byte N;
  static Set<Integer> cache = new HashSet<>();
  public static class E {
    short state;
    short mask;
    E(short state, short mask) {
        this.state = state;
        this.mask = mask;
    }
  }
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Byte.parseByte(br.readLine());
    byte[][] costs = new byte[N][N];
    byte answer = 1;
    Queue<E> q = new ArrayDeque<>();
    q.add(new E((short) 1, (short) 1));
    for (int i = 0; i < N; i++) {
      String[] input = br.readLine().split("");
      for (int j = 0; j < N; j++)
        costs[i][j] = Byte.parseByte(input[j]);
    }
    while (!q.isEmpty()) {
      E t = q.poll();
      int count = t.state & 0b1111;
      answer = (byte) Math.max(answer, count);
      for (short i = 0; i < N; i++) {
        int idx = (t.state >> 8) & 0b1111;
        int cost = (t.state >> 4) & 0b1111;
        short newState = (short) ((i << 8) | (costs[idx][i] << 4) | count + 1);
        short newMask = (short) (t.mask | (1 << i));
        if ((t.mask & (1 << i)) == 0 && cost <= costs[idx][i] && !cache.contains(newState << 16 | newMask)) {
          cache.add(newState << 16 | newMask);
          q.add(new E(newState, newMask));
        }
          
      }
    }
    System.out.println(answer);
  }
}