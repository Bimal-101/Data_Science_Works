#Task 2 - Q18 : Check subset

n = int(input())

for i in range(n):
    a = int(input())
    x = set(map(int, input().split()))
    b = int(input())
    y = set(map(int, input().split()))
    

    
    if x.intersection(y) == x:
        print("True")
    else:
        print("False")
