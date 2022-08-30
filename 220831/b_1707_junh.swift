
for _ in 1...Int(readLine()!)! {
    let input = readLine()!.split(separator: " ").map {
        Int($0)!
    }
    let v = input[0]
    let e = input[1]
    print(solve(v: v, e: e))
}



func solve(v: Int, e: Int) -> String {
    var graph = Array(repeating: [Int](), count: v+1)
    
    for _ in 1...e {
        let nums = readLine()!.split(separator: " ").map {Int($0)!}
        graph[nums[0]].append(nums[1])
        graph[nums[1]].append(nums[0])
    }
    
    var colors = [Int](repeating: 0, count: v+1)
    
    func bfs(start: Int) -> Bool {
        colors[start] = 1
        
        var q = [start], idx = 0
        
        while idx < q.count {
            let n = q[idx]
            let clr = colors[n]
            
            for i in graph[n] {
                if colors[i] == clr {
                    return false
                } else if colors[i] == 0 {
                    colors[i] = -clr
                    q.append(i)
                }
            }
            idx += 1
        }
        return true
    }
    
    for i in 1...v {
        if colors[i] == 0 && bfs(start: i) == false{
            return "NO"
        }
    }
    return "YES"
}

