x=input()
x=x.replace(" ","")
a=int(x,2)
a=hex(a)
a=a[2:]
a=bytes.fromhex(a).decode('utf-8')
print(a)