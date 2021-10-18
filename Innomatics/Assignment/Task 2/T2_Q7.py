#Task 2 - Q7 : Tuple


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    
    h = hash(t)
    print(h)
