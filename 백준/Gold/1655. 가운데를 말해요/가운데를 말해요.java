import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> smallNumbers = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> bigNumbers = new PriorityQueue<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            int t = Integer.parseInt(br.readLine());
            if (smallNumbers.isEmpty() || t < smallNumbers.peek())
              smallNumbers.add(t);
            else
              bigNumbers.add(t);

            if (smallNumbers.size() > bigNumbers.size() + 1)
              bigNumbers.add(smallNumbers.poll());
            else if (smallNumbers.size() < bigNumbers.size())
              smallNumbers.add(bigNumbers.poll());
            sb.append(smallNumbers.peek()).append("\n");
        }

        System.out.println(sb);
    }
}
