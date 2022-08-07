import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class b_16173_junh {
    static int N;
    static int[][] mat;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        mat = new int[N][N];

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j < N; j++){
                mat[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if (bfs()) {
            System.out.println("HaruHaru");
        } else {
            System.out.println("Hing");
        }
    }

    public static boolean bfs() {
        boolean[][] visited = new boolean[N][N];
        Queue<Point> q = new LinkedList<Point>();
        q.add(new Point(0, 0));
        visited[0][0] = true;

        while(!q.isEmpty()) {
            int x = q.peek().x;
            int y = q.peek().y;
            q.poll();
            int move = mat[y][x];

            int ny = y + move;
            if (ny < N && !visited[ny][x]){
                visited[ny][x] = true;
                if (ny == N-1 && x == N-1)
                    return true;
                q.add(new Point(x, ny));
            }

            int nx = x + move;
            if (nx < N && !visited[y][nx]){
                if (nx == N-1 && y == N-1)
                    return true;
                q.add(new Point(nx, y));
            }
        }
        return false;
    }
}