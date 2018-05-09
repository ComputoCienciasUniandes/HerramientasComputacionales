#punto 1
N=49
listapre=[1]
listapres=[1,1]
listapost=[]

#punto 2
for i in range(2,N):
	
	listapost=[1]
	for j in range(i-1):
		listapost.append(listapres[j]+listapres[j+1])
	listapost.append(1)

	listapre=list(listapres)
	listapres=list(listapost)

print(listapost)


#punto 3
x=str(listapost[int(len(listapost)/2)])
print(x,len(x))

#punto 3
x=str(listapost[int((N+1)/2 -1)])
print(x,len(x))




#punto 4
infile = open("code1.txt",'r')
lines= infile.readlines()
file.close()
print(lines)

###punto 5
for i in range(len(lines)):
	print(lines[i][int(x[i])])
