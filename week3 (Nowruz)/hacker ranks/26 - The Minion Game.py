def minion_game(string):

    vowel = 'aeiou'.upper()
    str_len = len(string)
    kevin = sum(str_len-i for i in range(str_len) if string[i] in vowel)
    stuart = str_len*(str_len + 1)/2 - kevin
    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
