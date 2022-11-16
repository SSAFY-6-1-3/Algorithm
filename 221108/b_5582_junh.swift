
let A = Array(" " + readLine()!)
let B = Array(" " + readLine()!)

var counts = Array(repeating: Array(repeating: 0, count: B.count), count: A.count)



for i in 1 ..< A.count {
    for j in 1 ..< B.count {
        if A[i] == B[j] {
            counts[i][j] = counts[i-1][j-1] + 1
        }
    }
}


print(
    counts.map { line in
        line.max()
    }.max(by: { a, b in
        a! < b!
    })!!
)
