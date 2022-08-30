
let input = readLine()!.split(separator: ":")
var m = Int(input[0])!
var s = Int(input[1])!

var cnt = 1

if s >= 30 {
    s -= 30
}

cnt += m/10 + m%10 + s/10

print(cnt)
