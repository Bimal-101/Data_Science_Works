#Task 2 - Q2 : Finding Runner Up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    Lis = list(arr)   
    Lis.sort()
    ind = Lis.index(max(Lis))

    print(Lis[ind -1])
