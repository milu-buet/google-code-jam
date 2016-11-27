#Author milu


N = int(input())
for i in range(N):
	words = [x for x in input().split()]
	words.reverse()
	ans = " ".join(words)

	out = "Case #%s: %s"%(i+1,ans)
	print(out)