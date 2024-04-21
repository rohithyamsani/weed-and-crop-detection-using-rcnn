def factors(n):
    ans = []
    for i in range(n//2):
        if n % 2 == 0:
            ans.append(i)
    return ans

l = list(map(int, input().split()))
ans = []
for i in range(l):
    ans.append(f'Multiple of ' + "".join(map(str, l)))
print(*l, sep = "\n")
