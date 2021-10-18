# Task 4 - Q9 : Designer DOOr

s = "WELCOME"
l = ".|."
n,m = map(int,input().split())

for i in range(1,int((n+1)/2)):
    c = l*(2*i-1)
    print(c.center(m,'-'))

print(s.center(m,'-'))

for i in range(int((n-1)/2),0,-1):
    c = l*(2*i-1)
    print(c.center(m,'-'))
