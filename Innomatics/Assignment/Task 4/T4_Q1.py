#Task 4 - Q1 : Swap Case


def swap_case(s):
    c = ""
    for i in s:
        if i.islower():
            c += i.upper()
        else:
            c += i.lower()
    return c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
