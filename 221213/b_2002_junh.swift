
let N = Int(readLine()!)!

var dg = [String]()
var ys = [String]()

for _ in 0 ..< N {
    dg.append(readLine()!)
}
for _ in 0 ..< N {
    ys.append(readLine()!)
}

var dic = [String:Int]()
for i in 0 ..< N {
    dic[dg[i]] = i
}
 
var answer = 0
for i in 0 ..< N {
    let org = dic[ys[i]]!
    for j in i+1 ..< N {
        if dic[ys[j]]! < org {
            answer += 1
            break
        }
    }
}
print(answer)

