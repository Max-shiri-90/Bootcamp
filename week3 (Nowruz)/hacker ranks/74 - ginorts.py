string = input()
low = []
upp = []
dig_o = []
dig_e = []

for i in string:
    if i.isalpha() and i.islower():
        low += i
    elif i.isalpha() and i.isupper():
        upp += i
    elif i.isdigit() and int(i)%2 != 0:
        dig_o += i
    elif i.isdigit() and int(i)%2 == 0:
        dig_e += i

low.sort()
upp.sort()
dig_o.sort()
dig_e.sort()
des_str = (low+upp+dig_o+dig_e)

print(''.join(des_str))
