input=raw_input()
a,b,c=input.split()
if(a>c) and (b>c):
    print(a)
elif(b>a) and (b>c):
    print(b)
else:
    print(c)
