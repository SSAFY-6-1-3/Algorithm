let NM = input()
let N = NM[0], M = NM[1]
var mat: [[Int]] = []

struct point {
    let y: Int
    let x: Int
    let n: Int
}
var houses: [point] = []
var chks: [point] = []

var chkN: Int = 1
for i in 0 ..< N {
    mat.append(input())
    for j in 0 ..< N {
        if mat[i][j] == 1 {
            houses.append(point(y: i, x: j, n: 0))
        }
        else if mat[i][j] == 2 {
            chkN  += 1
            chks.append(point(y: i, x: j, n: chkN))
        }
    }
}

var combs: [[Int]] = []
makeComb(idx: 1, comb: [])
var answer = N * N * N * N

for comb in combs {
    var cnt = 0
    for h in houses {
        var dist = N * N * N * N
        for ch in chks {
            if comb.contains(ch.n) {
                let d = abs(h.y - ch.y) + abs(h.x - ch.x)
                dist = min(dist, d)
            }
        }
        cnt += dist
    }
    answer = min(cnt, answer)
}
print(answer)




func input() -> [Int] {
    readLine()!.split(separator: " ").map { Int($0)! }
}

func makeComb(idx: Int, comb:[Int]) {
    if comb.count == M {
            combs.append(comb)
            return
    }
    else if idx + 1 > chkN {
        return
    }
    
    for i in idx+1 ... chkN {
        makeComb(idx: i, comb: comb + [i])
    }
}


//
//func bfs(y:Int, x: Int, comb: [Int]) -> Int {
//    let dY = [1, 0, -1, 0]
//    let dX = [0, 1, 0, -1]
//    var q = [(y, x, 0)]
//    var idx = 0
//    var visited: Set<[Int]> = Set()
//
//    while idx < q.count {
//        let (y, x, dist) = q[idx]
//        idx += 1
//
//        for d in 0 ..< 4 {
//            let (ny, nx) = (y + dY[d], x + dX[d])
//            if ny < 0 || ny >= N || nx < 0 || nx >= N || visited.contains([ny, nx]) {
//                continue
//            }
//            visited.insert([ny, nx])
//            if comb.contains(mat[ny][nx]) {
//                return dist + 1
//            }
//            q.append((ny, nx, dist + 1))
//        }
//    }
//    return 0
//}
