func inp() -> [String.SubSequence] {
    readLine()!.split(separator: " ")
}

let NK = inp()
let N = Int(NK[0])!
let K = Int(NK[1])!

var dp = Array(repeating: 0, count: K + 1)

for _ in 0 ..< N {
    let WV = inp()
    let W = Int(WV[0])!
    let V = Int(WV[1])!
    
    for s in stride(from: K - W, through: 0, by: -1) {
        if (s == 0 || dp[s] > 0) && dp[s] + V > dp[s + W] {
            dp[s + W] = dp[s] + V
        }
    }
}

print(dp.max()!)

