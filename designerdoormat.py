# Enter your code here. Read input from STDIN. Print output to STDOUT
i = input()
i = i.split()
n, m = int(i[0]), int(i[1])
pattern = []
for x in range(n//2):
    h = "-"*((m-3*(2*x+1))//2)
    dotslashdot = ".|."*((2*x)+1)
    pattern.append(h + dotslashdot + h)
for line in pattern:
    print(line)
h = "-"*((m-7)//2)
print(h + "WELCOME" + h)
pattern.reverse()
for line in pattern:
    print(line)
