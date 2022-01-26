from collections import Counter
#with open('input14-test.txt','r') as file:
with open('input14.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

startmol = lines[0]

lookup = dict()
for line in lines:
    if "->" not in line:
        continue
    lookup[line.split(" -> ")[0]]=line.split(" -> ")[1]

tmp_poly = Counter(a+b for a,b in zip(startmol, startmol[1:]))
print(tmp_poly)
chars = Counter(startmol)

for _ in range(40):
    tmp = Counter()
    for (c1,c2),value in tmp_poly.items():
        mc = lookup[c1+c2]
        tmp[c1+mc] += value
        tmp[mc+c2] += value
        chars[mc] += value
    tmp_poly=tmp

print(max(chars.values()) - min(chars.values()))


