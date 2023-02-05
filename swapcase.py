def swap_case(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += letter.lower()
        elif letter.islower():
            newStr += letter.upper()
        else:
            newStr += letter
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)