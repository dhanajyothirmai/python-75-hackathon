def myfunc(n):
    return lambda a : a * n

jyo = myfunc(3)
jyo1 = myfunc(2)
print(jyo(10))
print(jyo1(4)
