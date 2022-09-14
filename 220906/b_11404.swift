
let N = Int(readLine()!)!
let M = Int(readLine()!)!
var graph = Array(repeating: Array(repeating: 10000001, count: N), count: N)

func input() -> [Int] {
    readLine()!.split(separator: " ").map{Int($0)!}
}

func bfs(start: Int) {
    var q = Array(stride(from: 0, to: N, by: 1))
    var idx = 0
    
    while idx < q.count {
        let a = q[idx]
        idx += 1
        
        for b in 0..<N {
            if graph[start][a] + graph[a][b] < graph[start][b] {
                graph[start][b] = graph[start][a] + graph[a][b]
                q.append(b)
            }
        }
    }
}


for _ in 0 ..< M {
    let abc = input()
    let a = abc[0]-1, b = abc[1]-1
    graph[a][b] = min(graph[a][b], abc[2])
}

for i in 0 ..< N {
    graph[i][i] = 0
    bfs(start: i)
}

for i in 0 ..< N {
    for j in 0 ..< N {
        if i != j && graph[i][j] == 10000001 {
            graph[i][j] = 0
        }
    }
    print(graph[i].map({ String($0) }).joined(separator: " "))
}
