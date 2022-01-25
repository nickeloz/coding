import sys

crabs = {}
for i in map(int, sys.stdin.readline().split(',')):
    if i in crabs:
        crabs[i] += 1
    else:
        crabs[i] = 1
left, right = min(crabs.keys()), max(crabs.keys())

fuel = []
for i in range(left, right + 1):
    fuel.append(0)
    for (x, n) in crabs.items():
        fuel[-1] += abs(x - left - i) * n
print(min(fuel))