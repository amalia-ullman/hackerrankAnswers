def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = alphabet[size-1]
    lis = []
    for x in range(size,0,-1):
        h = "-"*(2*x-2)
        pattern = alphabet[size-1]
        if x < size:
            y = size-1
            while y >= x:
                pattern += "-"
                pattern += alphabet[y-1]
                y -= 1
            while x < size:
                pattern += "-"
                pattern +=  alphabet[x]
                x+=1
        lis.insert(0, h+pattern+h)
        print(h+pattern+h)
    for z in range(1, len(lis)):
        print(lis[z])
        
    

    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)