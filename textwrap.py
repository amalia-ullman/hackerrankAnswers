import textwrap

def wrap(string, max_width):
    newstr = ""
    w = 0
    for letter in string:
        newstr += letter
        w+=1
        if w == max_width:
            newstr += "\n"
            w=0
    return newstr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)