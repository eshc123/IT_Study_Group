# 신민희
# 2020-07-23(023)

import sys

N = int(sys.stdin.readline())

ans, i = 0,1

while i <=N:
    ans += (N-i+1)
    i *= 10

print(ans)

#https://rebas.kr/753


