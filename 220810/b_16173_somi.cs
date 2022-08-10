using System;

namespace bj
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int N;
            N = int.Parse(Console.ReadLine());
            int[,] map = new int[N, N];
            for (int i = 0; i < N; i++)
            {
                string[] tmp = Console.ReadLine().Split(' ');
                for (int j = 0; j < N; j++)
                {
                    map[i, j] = int.Parse(tmp[j]);
                }
            }

            int[] dx = new int[2] { 0, 1 };
            int[] dy = new int[2] { 1, 0 };
            bool[,] visited = new bool[N, N];
            bool flag = false;
            Queue<(int, int)> q = new Queue<(int, int)>();
            q.Enqueue((0, 0));
            visited[0, 0] = true;

            while (q.Count != 0)
            {
                var now = q.Dequeue();
                int x = now.Item1;
                int y = now.Item2;

                if (x == N - 1 && y == N - 1)
                {
                    Console.WriteLine("HaruHaru");
                    flag = true;
                    break;
                }

                for (int di = 0; di < 2; di++)
                {
                    int jump = map[x, y];
                    int nx = x + (dx[di] * jump);
                    int ny = y + (dy[di] * jump);

                    if (0 <= nx && nx < N && 0<= ny && ny < N && !visited[nx, ny])
                    {
                        q.Enqueue((nx, ny));
                        visited[nx, ny] = true;
                    }
                }
            }
            if (!flag)
            {
                Console.WriteLine("Hing");
            }
        }
    }
}