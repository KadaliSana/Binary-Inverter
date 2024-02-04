import base64

a="""This program can decode the following list:
1)Binary Inversion
2)Integer to Binary
3)Integer to Hexadecimal
4)Binary to Integer
5)Binary to Hexadeximal
6)Binary to ASCII
7)Hexadecimal to ASCII
8)Base 64 to ASCII"""
print(a)
y=input("Enter a number to choose the format to decode:")
x=input("Enter your Input:")
def BinInvert(x):
    x=list(x)
    a=""
    for i in range(len(x)):
        if x[i]=="0":
            x[i]="1"
        else:
            x[i]="0"
            a=a.join(x)
    return a

def BinASCII(x):
    x = x.replace(" ", "")
    a = int(x, 2)
    a = hex(a)
    a = a[2:]
    a = bytes.fromhex(a).decode('utf-8')
    return a

def BinHex(x):
    x = input()
    a = int(x, 2)
    a = hex(a)
    return a

def BinInt(x):
    a = int(x, 2)
    return a

def HexASCII(x):
    a = x.replace(" ", "")
    a = bytes.fromhex(a).decode('utf-8')
    return a

def IntBin(x):
    a = str(bin(int(x)))
    return a

def IntHex(x):
    a = str(hex(int(x)))
    return a

def Base64ASCII(x):
    a=base64.b64decode(x)
    return a

if y=="1":
    print(BinInvert(x))
elif y=="2":
    print(IntBin(x))
elif y=="3":
    print(IntHex(x))
elif y=="4":
    print(BinInt(X))
elif y=="5":
    print(BinHex(x))
elif y=="6":
    print(BinASCII(x))
elif y=="7":
    print(HexASCII(x))
elif y=="8":
    print(Base64ASCII(x))
