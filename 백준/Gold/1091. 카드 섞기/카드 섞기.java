import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    String[] input = br.readLine().split(" ");
    int[] P = new int[N];
    for (int i = 0; i < N; i++)
      P[i] = Integer.parseInt(input[i]);
    input = br.readLine().split(" ");
    int[] S = new int[N];
    for (int i = 0; i < N; i++)
      S[i] = Integer.parseInt(input[i]);
    int[] results1 = new int[N];
    List<Set<Integer>> results2 = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      int t = i;
      int count = 0;
      Set<Integer> tSet = new HashSet<>();
      while (true) {
        if (t % 3 == P[i])
          tSet.add(count);
        if (t == i && count != 0) {
          results1[i] = count;
          break;
        }
        if (count > 50) {
          results1[i] = 0;
          break;
        }
        t = S[t];
        count++;
      }
      results2.add(tSet);
    }

    boolean iter = true;
    
    for (int i = 0; i < N; i++) {
      if (results1[i] == 0) {
        iter = false;
        break;
      }
    }

    if (iter) {
      int result = 0;
      while (true) {
        boolean answer = true;
        for (int i = 0; i < N; i++)
          if (!results2.get(i).contains(result % results1[i]))
            answer = false;
        if (answer)
          break;
        if (result > 200000) {
          result = -1;
          break;
        }
        result++;
      }
      System.out.println(result);
    }
    else {
      Set<Integer> intersection = new HashSet<>(results2.get(0));
      for (int i = 1; i < N; i++)
        intersection.retainAll(results2.get(i));
      if (!intersection.isEmpty())
        System.out.println(Collections.min(intersection));
      else
        System.out.println(-1); 
    }
  }
}