#самое повторяемое слово в тексте
from collections import Counter
S = ""
with open("dataset_3363_1.txt") as inf:
    for line in inf:
        S += line.strip()

# S = input().strip()
d = {}
s = S.lower().split()
s.sort()
q = ""
n = ""

for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]] = d[s[i]] + 1

for key, value in d.items():
    n = key, value
    if len(q) != 0 and n < q:
        q = n
        n = ""
    else:
        q = key, value
    print(q)
a = Counter(d).most_common(1)
print(a)
print(len(d))
