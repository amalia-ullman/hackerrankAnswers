if __name__ == '__main__':
    l=[]
    nl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        nl.append(score)

i=[]
p=[]
t=[]
m=min(nl)

for x in range(0,len(l)):
    if nl[x] != m:
        p.append(l[x])
        t.append(nl[x])
for x in range(0,len(p)):
    if p[x][1] == min(t):
        i.append(p[x][0])
print("\n".join(sorted(i)))
