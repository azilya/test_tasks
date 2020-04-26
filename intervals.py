l = [1, 2, 3, 5, 6, 8]  # 1 2 3 5 7 8 9
ans = []
l.sort()
t = i = 0
s = str(l[0])
while i < len(l):
    if i + 1 < len(l) and l[i + 1] == l[i] + 1:
        i += 1
    else:
        if l[i] != l[t]: s += "-" + str(l[i])
        ans.append(s)
        t = i = i + 1
        if i < len(l):
            s = str(l[t])
print(", ".join(ans))