#Task 4 - Q5 : Find a string

def count_substring(string, sub_string):
    a = 0
    l1 = len(string)
    l2 = len(sub_string)
    for i in range(0,l1):
        if string[i:i+l2] == sub_string:
            a += 1
        
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
