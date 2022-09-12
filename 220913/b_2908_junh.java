import java.util.Scanner;

public class b_2908_junh {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = Integer.parseInt(new StringBuffer(sc.next()).reverse().toString());
        int b = Integer.parseInt(new StringBuffer(sc.next()).reverse().toString());

        System.out.println(Math.max(a, b));
    }
}
