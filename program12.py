j=int(raw_input())
k=0
l=j
while j!=0:
    o=j%10
    k=k*10+0
    j=j/10
if k==l:
        print("yes")
else:
        print("no")
