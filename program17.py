y=int(raw_input())
u=y%10
i=y/10
a=i%10
s=i/10
d=u**3+a**5+5**3
if(d==y):
    print("no")
else:
     print("yes")
