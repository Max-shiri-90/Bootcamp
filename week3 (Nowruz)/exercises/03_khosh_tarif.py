import re


def khosh_tarif(string):
    counter = 0
    lst = []

    for i in string:
        pattern = '[01/?]'
        result = re.match(pattern, i)
        if result:
            pass
        else:
            counter += 1
    if counter > 0:
        print("Wrong characters")
    else:
        j = 0
        if string[0] == '0':  # starting with 0
            while j < len(string):
                if j % 2 == 0:
                    if string[j] == '0':
                        lst.append(string[j])
                    elif string[j] == '1':
                        pass
                    elif string[j] == '?':
                        string.replace(string[j], '0')
                        lst.append(string[j])
                elif j % 2 != 0:
                    if string[j] == '1':
                        lst.append(string[j])
                    elif string[j] == '0':
                        pass
                    elif string[j] == '?':
                        string.replace(string[j], '1')
                        lst.append(string[j])
                j += 1

        elif string[0] == '1':  # starting with 1
            while j < len(string):
                if j % 2 == 0:
                    if string[j] == '1':
                        lst.append(string[j])
                    elif string[j] == '0':
                        pass
                    elif string[j] == '?':
                        string.replace(string[j], '1')
                        lst.append(string[j])
                elif j % 2 != 0:
                    if string[j] == '0':
                        lst.append(string[j])
                    elif string[j] == '1':
                        pass
                    elif string[j] == '?':
                        string.replace(string[j], '0')
                        lst.append(string[j])
                j += 1

        elif string[0] == '?':  # starting with ?
            if string.count(i) == len(string):
                for j in string:
                    lst.append(j)
            else:
                print('')

    if len(lst) == len(string):
        print('Khosh Tarif')
        print(lst)
    elif len(lst) != len(string):
        print('Not Khosh Tarif')


khosh_tarif(string=input())


