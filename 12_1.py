from collections import defaultdict

paths = defaultdict(list)
#for a,b in [line.split('-') for line in open('input12-test.txt').read().splitlines()]:
for a,b in [line.split('-') for line in open('input12.txt').read().splitlines()]:
    paths[a].append(b)
    paths[b].append(a)

def dfs(cave, visited, one_off):
    if (cave == 'end'): return 1
    if (cave.islower()): visited.add(cave)
    total = sum([dfs(i, visited, one_off) for i in paths[cave] if not i in visited])
    total += sum([dfs(i, visited, i) for i in paths[cave] if i in visited and i != 'start']) if one_off == ' ' else 0
    if (cave != one_off): visited.discard(cave)
    return total;

print ('Part 1:', dfs('start', set(), ''))
print ('Part 2:', dfs('start', set(), ' '))
