try:
    for _ in range(int(input())):
        h, c, t = map(float, input().split())
        if h > 50.0 and c < 0.7 and t > 5600:
            grade = 10
        elif h > 50.0 and c < 0.7:
            grade = 9
        elif c < 0.7 and t > 5600:
            grade = 8 
        elif h > 50.0 and t > 5600:
            grade = 7
        elif h > 50.0 or c < 0.7 or t > 5600:
            grade = 6
        else:
            grade = 5 
        print(grade)
except:
    pass
