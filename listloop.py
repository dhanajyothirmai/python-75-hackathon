jyo = [2,7.3,8,7,]
total = 0
i = 0
while i < len(jyo):
    total = total + jyo[i]
    i = i + 1
print(total)
average = total / len(jyo)
print(average)
print(average*3)

def double(x):
 return x*2

print(double(10))

l = [double(x) for x in range(10)]

print(l)

l2= [double(x) for x in range(10) if x%2==0]
print(l2)

l3=[x+y for x in [10,30,50] for y in [20,40,60]]
print(l3)
