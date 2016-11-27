# Author : Milu





def minPair(C,I,P1):

	P = sorted(P1)
	for i in range(I-1):
		j=i+1
		while(j<I and P[i] + P[j] < C):
			j+=1

		if j<I and P[i] + P[j] == C:
			a1_val = P[i]
			a2_val = P[j]
			if a1_val == a2_val:
				a1 = P1.index(P[i])
				P1.pop(a1)
				a2 = P1.index(P[j]) + 2

				return a1+1,a2
			else:
				a1 = P1.index(P[i])+1
				a2 = P1.index(P[j])+1
				return min(a1,a2),max(a1,a2)


	return None,None



N = int(input())

for i in range(N):
	C = int(input())
	I = int(input())

	P = [int(x) for x in input().split()]
	#print(P)

	a1,a2 = minPair(C,I,P)
	out = "Case #%s: %s %s"%(i+1,a1,a2)
	print(out)
	