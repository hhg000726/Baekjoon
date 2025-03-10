import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int answer = 0;
        List<List<Integer>> lamp = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            List<Integer> newList = new ArrayList<>();
            for (char a : br.readLine().toCharArray())
                newList.add(Character.getNumericValue(a));
            lamp.add(newList);
        }
        int K = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            List<Integer> t = lamp.get(i);
            List<Integer> indexes = new ArrayList<>();
            int count = 0;
            for (int j = 0; j < M; j++) {
                if (t.get(j) == 0) {
                    indexes.add(j);
                    count += 1;
                }
            }
            if (K >= count && (K - count) % 2 == 0) {
                List<List<Integer>> changed = new ArrayList<>();
                for(List<Integer> list : lamp)
                    changed.add(new ArrayList<>(list));
                int tanswer = 0;
                for (List<Integer> list : changed)
                    if (changed.get(i).equals(list))
                        tanswer += 1;
                answer = Math.max(answer, tanswer);
            }
        }
        System.out.print(answer);
    }
}