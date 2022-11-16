import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_9935_junh {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine();
        String boom = br.readLine();
        StringBuilder sb = new StringBuilder();

        for (char c : st.toCharArray()) {
            sb.append(c);
            if (sb.length() >= boom.length()) {
                boolean isSame = true;
                for (int i=0; i < boom.length(); i++) {
                    if (sb.charAt(sb.length() - boom.length() + i) == boom.charAt(i)) {
                        continue;
                    } else {
                        isSame = false;
                        break;
                    }
                }
                if (isSame) {
                    sb.delete(sb.length() - boom.length(), sb.length());
                }
            }
        }

        if (sb.length() > 0) {
            System.out.println(sb.toString());
        } else {
            System.out.println("FRULA");
        }
    }
}
