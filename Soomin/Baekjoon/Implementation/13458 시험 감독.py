#13458
#삼성기출

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

ans = n
for i in range(n):
  aa = a[i] - b
  if aa > 0:
    an = aa // c
    ans += an
    if aa % c != 0:
      ans += 1

print(ans)