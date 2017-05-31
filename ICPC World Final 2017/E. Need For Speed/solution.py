#! /usr/bin/python3


def getApproxSum(n,t,rows,c):
	fsum = 0
	for i in rows:
		if (rows[i]['s'] + c) !=0:
			fsum+=rows[i]['d']/(rows[i]['s'] + c)
		else:
			fsum+=100001000
	return fsum

def getAns(n,t,rows,c1,c2):

	if c1 >= c2:
		return c1

	cmid = (c1+c2)/2  # a2<t<a1
	approx = getApproxSum(n,t,rows,cmid)

	if abs(t - approx) < 0.000000001:
		return cmid

	#print(cmid)

	if t < approx:
		return getAns(n,t,rows,cmid,c2)
	else:
		return getAns(n,t,rows,c1,cmid)

def getAnsI(n,t,rows,c1,c2):

	while(c2-c1 > 0.000000001):

		cmid = (c1+c2)/2  # a2<t<a1
		approx = getApproxSum(n,t,rows,cmid)
		
		if t < approx:
			c1 = cmid
		else:
			c2 = cmid

	return (c1 + c2)/2



while True:
	try:
		n,t  =  [int(x) for x in input().split()]
	except:
		break
	rows = {}
	min_s = -100000000
	for j in range(n):
		rows[j] = {}
		rows[j]['d'], rows[j]['s'] = [int(x) for x in input().split()]

		min_s = max(min_s,-rows[j]['s'])

	try:
		ans = getAnsI(n,t,rows,min_s,100001000)
		out = "%.9f"%(ans,)
	except:
		break

	#print(out)
	print(out)