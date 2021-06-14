s = []
S = []
with open("dataset_3363_1.txt") as inf:
    for line in inf:
        s = line.strip().split(";")
        S.append(s)
        a = (int(s[1]) + int(s[2]) + int(s[3])) / 3  # средня оценка студента

print(S)
print(a)
print(s)
