x,y=raw_input().split()
x=int(x)
y=int(y)
for m in range(x+1,y):
    if m>1:
        for i in range(2,m):
            if(m%i==0):
                break
            else:
                print(m),
