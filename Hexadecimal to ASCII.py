x=input()
a=x.replace(" ","")
a=bytes.fromhex(a).decode('utf-8')
print(a)