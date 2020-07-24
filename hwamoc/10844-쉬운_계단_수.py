'''
# 예제 입력 1
1
# 예제 입력 2
2
'''
from sys import stdin, stdout
input = stdin.readline

# 끝자리가 0~9일 때 개수를 모두 따져본다.
# nc[i][j]는 i자리 수에서 j로 끝나는 수들의 총 개수
# 0과 9는 자리수가 늘어나도 1과 8만 올 수 있지만 2~8의 경우 다음 자리 수에 1,3 2,4  3,5등 두가지 경우를 가진다.
# 자릿수가 i일 때 -> 자릿수 i-1일 때 앞(j-1) + 뒤(j+1)의 갯수를 합친 경우의 수를 가진다.
# 점화식: nc[i][j] = nc[i-1][j-1] + nc[i-1][j+1]
N = int(input())
nc = [[0]*10 for _ in range(N+1)]
mod = 1000000000
nc[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, N+1):
  for j in range(10):
    if j == 0:
      nc[i][j] = nc[i-1][1] % mod
    elif j == 9:
      nc[i][j] = nc[i-1][8] % mod
    else:
      nc[i][j] = (nc[i-1][j-1] + nc[i-1][j+1]) % mod
print(sum(nc[N])%mod)


'''
a=1;b=c=d=e=2
for i in range(int(input())-1):a,b,c,d,e=b,a+c,b+d,c+e,d+e
print((a+b+c+d+e)%1000000000)
'''