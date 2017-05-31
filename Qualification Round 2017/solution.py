#Author milu


def getAns(N,M,rows):
	pass


T = int(input())
for i in range(T):
	N,M  =  [int(x) for x in input().split()]
	rows = {}
	for i in range(M):
		rows[i] = [x for x in input().split()]

	ans = getAns(N,M,rows)
	out = "Case #%s: %s"%(i+1,ans)
	#print(out)
	print(M)