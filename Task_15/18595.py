from itertools import combinations


def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not(C or J)) <= (not A)


ans = []
line = [i / 4 for i in range(47 * 4, 101 * 4)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))

#Ответ: 52
