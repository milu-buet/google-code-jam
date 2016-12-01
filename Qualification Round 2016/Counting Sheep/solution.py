#Author milu



def getSheep(n):
	
	if n == 0:
		return "INSOMNIA"

	collected = []

	i = 1
	while(True):
		new_n = i*n
		for c in str(new_n):
			if c not in collected:
				collected.append(c)
		#print(collected)

		if len(collected) == 10:
			return new_n

		i+=1




T = int(input())
for i in range(T):
	number  = int(input())
	ans = getSheep(number)
	out = "Case #%s: %s"%(i+1,ans)
	print(out)