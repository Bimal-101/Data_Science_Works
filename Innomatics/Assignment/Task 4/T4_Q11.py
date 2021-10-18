#Task 4 - Q11 : Alphabet rangoli

def print_rangoli(size):
    x = []
    for i in range(97,size+97):
        x += chr(i)   
    
    m = 4*(size-1)+1
    
    #Upper
    q = []
    for j in range(1,size):
        o = x[size-1:size-j:-1]
        p = x[size-j:size]
        q = '-'.join(o+p).center(m,'-')
        print(q)
    
    #Lower
    f = []
    for k in range(size,0,-1):
        c = x[size-1:size-k:-1]
        d = x[size-k:size]
        f = '-'.join(c+d).center(m,'-')
        print(f)
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
