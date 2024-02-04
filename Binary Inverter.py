x=input()
x=list(x)
a=""
for i in range(len(x)):
    if x[i]=="0":
        x[i]="1"
    else:
        x[i]="0"
a=a.join(x)
print(a)