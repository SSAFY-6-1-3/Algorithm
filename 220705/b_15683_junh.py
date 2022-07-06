
cam_dic = {
    1 : ((0, 1)),
    2 : ((0, 1), (0, -1)),
    3 : ((0, 1), (1, 0)),
    4 : ((0, -1), (1, 0), (0, 1)),
    5 : ((1, 0), (0, 1), (-1, 0), (0, -1))
}

N, M = map(int, input().split())
checked = [[0]*M for _ in range(N)]
mat = []
cam = []

for i in range(N):
    line = list(map(int, input().split()))
    mat.append(line)
    for j in range(M):
        if line[j] in range(1, 6):
            cam.append([i, j, line[j]])
            line[j] = 1


def check(cam_num):
    y, x, code = cam[cam_num]

    cam_dir = cam_dic[code][:]

print(mat)
print(cam)
