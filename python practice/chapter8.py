for dan in range(2,10):
    i = 1
    for i in range(1,10):
        if dan%2 == 0:
            continue
        elif dan == i-1:
            print()
            break
        else:
            print(f'{dan} X {i} = {dan * i}')
            
            
    
