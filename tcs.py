def fun():
    lst1 = []
    n = int(input())
    if n < 2:
        print("invalid input")
        return 0
    else:
        for i in range(n):
            number = int(input())
            lst1.append(number)
        flag=0
        for i in range(n):
            if lst1[i]!=lst1[0]:
                flag+=1
                break
        if flag==0:
            print("Equal")
            return 0

        lst1.sort()
        print(lst1[0],lst1[1])

fun()