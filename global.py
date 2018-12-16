a = 435
c = 89
b = 39
def glob():
    global a,b,c
    a = 45
    b = a 
    c = a+b

glob()
print(a)
print(b)
print(c)
