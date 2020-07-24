import sys

M = int(sys.stdin.readline())
N = M // 2

stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]

newstat = [i+ j for i, j in zip(row, col)]
allstat = sum(newstat) // 2
newstat.sort()

def main(addup, i):
    if addup >= 0:
        return -addup
    if i == -1:
        return addup
    x = main(addup + newstat[i], i-1)
    if x == 0:
        return 0
    return max(x, main(addup, i-1))

print(-main(-allstat, M - 2))