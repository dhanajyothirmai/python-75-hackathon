def jyo(x):
    return lambda a : a + x

y = jyo(10)

print(y(45))
