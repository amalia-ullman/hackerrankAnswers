if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
oldList = list(map(int, arr))
newList = []
for x in range(0,n):
    if oldList[x] not in newList:
        if len(newList) == 2:
            if oldList[x] > newList[0]:
                newList.insert(0, oldList[x])
                newList.pop(2)
            elif oldList[x] > newList[1]:
                newList.pop(1)
                newList.append(oldList[x])
        if len(newList) == 1:
            if oldList[x] > newList[0]:
                newList.insert(0, oldList[x])
            else:
                newList.append(oldList[x])
        if len(newList) == 0:
            newList.append(oldList[x])
print(newList[1])

# could've literally just used max() but yk
