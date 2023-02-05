if __name__ == '__main__':
    s = input()
    alpha, alpha_bet, digit, low, up = False, False, False, False, False
    for x in s:
        if alpha == False:
            alpha = x.isalnum()
        if alpha_bet == False:
            alpha_bet = x.isalpha()
        if digit == False:
            digit = x.isdigit()
        if low == False:
            low = x.islower()
        if up == False:
            up = x.isupper()
    
    print(alpha)
    print(alpha_bet)
    print(digit)
    print(low)
    print(up)
