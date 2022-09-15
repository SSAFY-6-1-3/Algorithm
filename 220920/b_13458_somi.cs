using System;
namespace baekjoon
{
    class Program
    {
        static void Main()
        {
            int N = int.Parse(Console.ReadLine());
            string[] input = Console.ReadLine().Split();

            string[] BC = Console.ReadLine().Split();
            int B = int.Parse(BC[0]);
            int C = int.Parse(BC[1]);

            long ans = N;

            for(int i = 0; i < N; i++)
            {
                int restStudent = int.Parse(input[i]) - B;
                if (restStudent > 0)
                {
                    if (restStudent % C == 0)
                    {
                        ans += restStudent / C;
                    }
                    else
                    {
                        ans += (restStudent / C) + 1;
                    }

                }
            }

            Console.WriteLine(ans);


        }
    }
}
