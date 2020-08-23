try:
    for _ in range(int(input())):
        S = input()
        activities = ['C','E','S']
        for i in S:
            if i not in activities:
                print('no')
                break
            while i != activities[0]:
                del activities[0]
        else:
            print('yes')
except:
    pass
