import java.util.Arrays;
import java.util.Scanner;
import java.math.BigInteger;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String[] arr = new String[N];
    for (int i = 0; i < N; i++) {
      arr[i] = sc.next();
    }
    int K = sc.nextInt();
    sc.close();

    BigInteger[] potentials = new BigInteger[36];
    Arrays.fill(potentials, BigInteger.ZERO);

    for (int i = 0; i < N; i++) {
      String s = arr[i];
      for (int j = 0; j < s.length(); j++) {
        int index = Character.isDigit(s.charAt(j)) ? s.charAt(j) - '0' : s.charAt(j) - 'A' + 10;
        potentials[index] = potentials[index].add(BigInteger.valueOf(35 - index).multiply(BigInteger.valueOf(36).pow(s.length() - j - 1)));
      }
    }

    BigInteger sum = new BigInteger("0", 10);
    for (int i = 0; i < N; i++) {
      BigInteger val = new BigInteger(arr[i], 36);
      sum = sum.add(val);
    }

    Arrays.sort(potentials);
    for (int i = 0; i < K; i++)
      sum = sum.add(potentials[35 - i]);

    System.out.println(sum.toString(36).toUpperCase());
  }
}