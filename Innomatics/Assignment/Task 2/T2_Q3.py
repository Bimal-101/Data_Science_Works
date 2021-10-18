#Task 2 -Q3 : Nested Lists

if __name__ == '__main__':
    l1 = []
    l2 = []
    l3 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append([name,score])
        l2.append(score)
    
    l4 = list(set(l2))
    l4.sort()
    
    for name,score in l1:
        if score == l4[1]:
            l3.append(name)
    
    l3.sort()
    for i in l3:
        print(i)
