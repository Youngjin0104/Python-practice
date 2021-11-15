with open('test.txt', 'rt') as source:
    cnt1 = 0
    while True:
        line = source.readline()
        if not line:
            break
        source1 = line.split(',')
        cnt = source1[3]
        for i in range(len(cnt)):
            if cnt[i] != cnt[0]:
                cnt1 += int(cnt)
                
    print(f'모두의 나이의 합은 {cnt1}입니다.')
