star = '*'
space = ' '
i = 1
j = 3
while i <= 7:
    print(space *j, star*i)
    i += 2
    j -= 1
    if i == 7:
        while i >= 0 :
            print(space * j, star *i)
            i -= 2
            j += 1
        break
