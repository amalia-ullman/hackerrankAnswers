def count_substring(string, sub_string):
    count = 0
    for x in range(0, (len(string))-(len(sub_string))+1):
        if string[x] == sub_string[0]:
            match = True
            for y in range(1, len(sub_string)):
                if string[x+y] != sub_string[y]:
                    match = False
                    break
            if match == True:
                count +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)