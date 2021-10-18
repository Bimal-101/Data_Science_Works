#Task 2 - Q6 : Lists

if __name__ == '__main__':
    
    lis = []

    N = int(input())
    for i in range(N):
        a = input().split()
        
        if a[0] == "insert":
            x = int(a[1])
            y = int(a[2])
            lis.insert(x,y)
        elif a[0] == "print":
            print(lis)
        elif a[0] == "remove":
            x = int(a[1])
            lis.remove(x)
        elif a[0] == "append":
            x = int(a[1])
            lis.append(x)
        elif a[0] == "sort":
            lis.sort()
        elif a[0] == "pop":
            lis.pop()
        elif a[0] == "reverse":
            lis.reverse()
        
