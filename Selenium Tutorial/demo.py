
n = int(input())

for i in range(n):
    f_input = [int(num) for num in input().split(" ")]
    t_series = f_input[0]
    command = f_input[1]

    series = [int(num) for num in input().split(" ")]

    sumx = []
    for j in range(command):
        add = 0
        comnd = input().split(" ")
    
        if comnd[0] == "Q":
            s = query(int(comnd[1]),int(comnd[2]),series)
            add = add + int(s)
    
        elif comnd[0] == "U":
            series[int(comnd[1])-1] = int(comnd[2])
        sumx.append(add)
    total = sum(sumx)
    
    print("Case #{}: {}".format(i+1,total))