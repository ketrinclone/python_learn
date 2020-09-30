def Hckfest():
    i = 1
    while i == 1:
        rows1 = 5
        for crit in range(1, rows1+1):
            for column in range(1, crit+1):
                print(column, end=" ")
            print(" ")
        print("1 2 3 4 5 6")
        rows3 = 5
        c = rows3
        for crit2 in range(rows3, 0, -1):
            for column2 in range(0, crit2):
                print(c, end=' ')
            print("\r")
        continue