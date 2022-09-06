let N = Int(readLine()!)!
let m = 1000000007



func matMulti(mat1: Array<Array<Int>>, mat2: Array<Array<Int>>) -> Array<[Int]> {
    var ans = Array<[Int]>()
    
    for i in 0 ..< mat1.count {
        ans.append([Int]())
        for j in 0 ..< mat2[0].count {
            var tmp = 0
            for k in 0 ..< mat1[0].count {
                tmp += mat1[i][k] * mat2[k][j]
            }
            ans[i].append(tmp % m)
        }
    }
    return ans
}

func solve(mat: [[Int]], p: Int) -> [[Int]] {
    
    if p == 1 {
        return mat
    } else {
        let tmp = solve(mat: mat, p: p/2)
        
        if p % 2 == 0 {
            return matMulti(mat1: tmp, mat2: tmp)
        } else {
            return matMulti(mat1: matMulti(mat1: tmp, mat2: tmp), mat2: mat)
        }
    }
}

let matrix = [[1, 1], [1, 0]]
print(solve(mat: matrix, p: N)[0][1])
