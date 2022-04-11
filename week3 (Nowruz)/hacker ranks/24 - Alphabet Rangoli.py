import string

def print_rangoli(size):
    lower_alphabet =string.ascii_lowercase[0:size]
    
    for i in range(size-1, -size, -1):
        j = abs(i)
        line = lower_alphabet[size:j:-1] + lower_alphabet[j:size]
        print ("--"*j+ '-'.join(line)+"--"*j)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
