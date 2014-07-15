# Units converter

x = []

for i in range(100):
    x.append(i)

y = 0
z = []

for i in range(len(x)):
    if(x[i]%3 == 0):
        z.append(x[i])
print z
print sum(z)

