#Task 4 - Q12 : Capitalise

def solve(s):
    s1 = []
    s2 = s.split(' ')
    for i in s2:
        k = i.capitalize()
        s1 += [k]
    
    return(' '.join(s1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
