# Task 4 - Q10 : String Formatting - Prototype

def print_formatted(number):
    e = len(bin(number))-2
    for i in range(1,n+1):
        a = str(i)
        b = str(oct(i))
        c = str(hex(i))
        d = str(bin(i))
        
        
        
        print(a.rjust(e," "), b[2:].rjust(e," "), c[2:].rjust(e," ").upper(), d[2:].rjust(e," "))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
