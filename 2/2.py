def searchMax(inputLine):
	n = inputLine[0]
	inputLine.append(0)
	cache = [0, 0]
	for i in range(1, n+2):
		tmp = max(cache[0],cache[1]) + inputLine[i]
		cache[0] = cache[1]
		cache[1] = tmp
	return cache[1]

f = open('in','r') 
inputLine = []
for i in f.read().split():
	inputLine.append(int(i))
f.close()

result = searchMax(inputLine)

f = open('out','w')
f.write(str(result))
f.close()

print result
