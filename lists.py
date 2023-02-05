if __name__ == '__main__':
    N = int(input())
    cmds = []
    for i in range(0,N):
        cmds.append(input())
    
list=[]
for x in range(0,len(cmds)):
    if "append" in cmds[x]:
        sp = cmds[x].split()
        list.append(int(sp[1]))
        #print(sp[1])
    if "insert" in cmds[x]:
        sp = cmds[x].split()
        list.insert(int(sp[1]), int(sp[2]))
        #print(list)
    if "remove" in cmds[x]:
        sp = cmds[x].split()
        list.remove(int(sp[1]))
        #print(int(sp[1]))
    if "print" in cmds[x]:
        print(list)
        #list=[]
    if "sort" in cmds[x]:
        list.sort()
    if "pop" in cmds[x]:
        list.pop()
    if "reverse" in cmds[x]:
        list.reverse()
