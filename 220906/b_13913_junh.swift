let Inp = readLine()!.split(separator: " ").map { Int($0)!}
let N = Inp[0], K = Inp[1]

var dp = Array(repeating: (from: 0,step: -1), count: 100001) // (from, step)
dp[N] = (from: N, step: 0)

if N == K {
    print(0)
    print(N)
}
else if N > K {
    print(N - K)
    var route = ""
    for i in stride(from: N, to: K-1, by: -1) {
        route.append(i.description + " ")
    }
    print(route)
}
else {
    print(bfs())
    print(route())
}

func bfs() -> Int{
    var q = [N]
    var idx = 0

    while idx < q.count {
        let now = q[idx], step = dp[now].step
        
        
        for next in [now-1, now+1, now*2] {
            if next < 0 || next > 100000 {
                continue
            }
            if next == K {
                dp[next] = (from: now, step: step+1)
                return step + 1
            }
            if dp[next].step == -1 {
                dp[next] = (from: now, step: step+1)
                q.append(next)
            }
        }
        idx += 1
    }
    return -1
}

func route() -> String {
    var stack = [K]
    
    var tmp = K
    
    while dp[tmp].from != tmp {
        tmp = dp[tmp].from
        stack.append(tmp)
    }
    var ret = ""
    while !stack.isEmpty {
        ret.append(stack.popLast()!.description + " ")
    }
    return ret
}
