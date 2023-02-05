if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
list1 = []
for i in range(0, x+1):
    list1.append(i)

list2 = [[p,j,k] for p in list1 for j in range(0,y+1) for k in range(0,z+1)]

            
last = [s for s in list2 if s[0]+s[1]+s[2]!=n]
print(last)
