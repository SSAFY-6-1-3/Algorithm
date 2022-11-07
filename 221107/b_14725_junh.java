import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class b_14725_junh {
    static StringBuilder sb;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        HashMap<String, HashMap> root = new HashMap<>();

        for (int i=0; i < N; i++) {
            int K = sc.nextInt();
            HashMap parent = root;
            for (int j=0; j < K; j++) {
                String food = sc.next();
                HashMap target = (HashMap)parent.get(food);
                if (target == null) {
                    parent.put(food, new HashMap<>());
                    target = (HashMap)parent.get(food);
                }
                parent = target;
            }
        }
        sb = new StringBuilder();

        dfs(root, 0);
        System.out.println(sb.toString().strip());
    }

    static void dfs(HashMap<String, HashMap> parent, int depth) {
        String[] keys = parent.keySet().toArray(new String[0]);
        Arrays.sort(keys);
        for (String key : keys) {
            sb.append("\n");
            for (int i=0; i<depth; i++) {
                sb.append("--");
            }
            sb.append(key);
            dfs(parent.get(key), depth + 1);
        }

    }
}
