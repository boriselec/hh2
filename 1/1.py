brAll = [1]
brSquare = [1]

def calcAll(length):
	global brAll, brSquare
	for i in range(1, length+1):
		currSquare = brSquare[i-1]*(4*i-2)/(i+1)% 1000000007
		brSquare.append(currSquare)
		curr = 0
		for j in range(0, i):
			curr += (brSquare[j] + brAll[j])*brAll[i-j-1]
		curr = curr % 1000000007
		brAll.append(curr)
	print brAll
	return brAll[length]

f = open('in','r') 
n = int(f.read().split()[0])
f.close()

result = calcAll(n)

f = open('out','w')
f.write(str(result))
f.close()

print result
