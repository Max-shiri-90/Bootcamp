def swap_case(s):
    num = ""
    for elm in s:
        if elm.isupper() == True:
            num += (elm.lower())
        else:
            num += (elm.upper())
    return num
    
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
