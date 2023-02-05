def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    for x in range(0, len(string)):
        if string[x] in vowels:
            kevin += len(string) - x
        else:
            stuart += len(string) - x
    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif stuart > kevin:
        print("Stuart " + str(stuart))
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)