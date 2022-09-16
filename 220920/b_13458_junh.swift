let N = Int(readLine()!)!
let A = readLine()!.split(separator: " ").map { Int($0)!}
let BC = readLine()!.split(separator: " ").map { Int($0)!}
let B = BC[0], C = BC[1]
var cnt = 0

for i in 0 ..< N {
    let stu = A[i] - B
    cnt += 1
    if stu > 0 {
        cnt += stu / C + (stu % C > 0 ? 1 : 0)
    }
}
print(cnt)

