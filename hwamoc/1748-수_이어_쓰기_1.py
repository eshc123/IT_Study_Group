'''
# 예제 입력 1
120
'''
from sys import stdin, stdout
input = stdin.readline

n = int(input())
l = len(str(n))

ans = 0

for i in range(1, l+1):
  stri = '9'* i
  inti = int(stri)
  if n > inti:
    ans += 10**(i-1) * 9 * i
  else:
    te = n - 10**(i-1)
    ans += te * i
    break

print(ans + l)