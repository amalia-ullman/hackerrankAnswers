# Enter your code here. Read input from STDIN. Print output to STDOUT
css = input()
inp = ""
numOfLine = int(css)
brace = 0
numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letter = ["a", "b", "c", "d", "e", "f"]
hexValues = []
output = ""

for a in range(numOfLine):
    b = input()
    inp += b


for x in range(len(inp)-1):
    if inp[x] == "{":
        brace +=1
    if inp[x] == "}":
        brace-=1
    if inp[x] == "#" and brace == 1:
        if inp[x+1] in numb or inp[x+1].lower() in letter:
            if inp[x+2] in numb or inp[x+2].lower() in letter:
                if inp[x+3] in numb or inp[x+3].lower() in letter:
                    if inp[x+4] in numb or inp[x+4].lower() in letter:
                        if inp[x+5] in numb or inp[x+5].lower()in letter:
                            if inp[x+6] in numb or inp[x+6].lower() in letter:
                                y = inp[x] + inp[x+1] + inp[x+2] + inp[x+3] + inp[x+4] + inp[x+5] + inp[x+6]
                                hexValues.append(y)
                    else:
                        y = inp[x] + inp[x+1] + inp[x+2] + inp[x+3]
                        hexValues.append(y)
output += "\n".join(hexValues)
print(output)
