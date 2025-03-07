import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Set<String> Ns = new HashSet<>();
    Ns.add(scanner.next());
    int K = scanner.nextInt();
    scanner.close();

    while (K > 0) {
      Set<String> newNs = new HashSet<>();
      for (String N : Ns) {
        for (int i = 0; i < N.length() - 1; i++) {
          for (int j = i + 1; j < N.length(); j++) {
            if (i == 0 && N.charAt(j) == '0') {
              continue;
            }
            String newN = N.substring(0, i) + N.charAt(j) + N.substring(i + 1, j) + N.charAt(i) + N.substring(j + 1);
            newNs.add(newN);
          }
        }
      }
      K--;
      if (newNs.isEmpty()) {
        newNs.add("-1");
        Ns = newNs;
        break;
      }
      Ns = newNs;
    }

    System.out.println(Ns.stream().mapToInt(Integer::parseInt).max().getAsInt());
  }
}