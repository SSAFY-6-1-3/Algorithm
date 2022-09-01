
let inp = readLine()!.split(separator: " ").map { Int($0)!}
var N = inp[0], M = inp[1]
var mat = Array<Array<Character>>()
var power: [Character:Int] = ["W": 0, "B": 0]
for _ in 1...M {
    mat.append(Array(readLine()!))
}
let dY = [0, 1, 0, -1]
let dX = [1, 0, -1, 0]

for i in 0...M-1 {
    for j in 0...N-1 {
        if mat[i][j] != "X"{
            bfs(sY: i, sX: j)
        }
    }
}

print(power["W"]!, power["B"]!)


func bfs(sY: Int, sX: Int) {
    let color = mat[sY][sX]
    mat[sY][sX] = "X"
    var point = 1

    var q = [(sY, sX)]
    var idx = 0
    
    while idx < q.count {
        let y = q[idx].0, x = q[idx].1
        idx += 1
        
        for d in 0...3 {
            let ny = y + dY[d], nx = x + dX[d]
            if (ny < 0) || (ny >= M) || (nx < 0) || (nx >= N) {
                continue
            }
            if mat[ny][nx] == color {
                q.append((ny, nx))
                mat[ny][nx] = "X"
                point += 1
            }
        }
    }
    power[color]? += point * point
}

