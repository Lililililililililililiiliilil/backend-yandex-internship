n = int(input())
volume = list(map(int, input().split()))

flag = 0

for i in range(len(volume) - 1):
    if volume[i] <= volume[i + 1]:
        flag += 1

if flag != len(volume) - 1:
    print(-1)
else:
    flag = 0
    max_vol = max(volume)
    for i in range(len(volume) - 1):
        if volume[i] < volume[i + 1]:
            flag += volume[i + 1] - volume[i]
    print(flag)
