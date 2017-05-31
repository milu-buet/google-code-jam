#print 'run...'


cr_pm = [-1]*4

def print_perm(istr):
	p_str = ''
	for i in cr_pm:
		p_str = p_str + istr[i]

	print(p_str)

def perm(istr,ind):

	if ind == len(istr):
		print_perm(istr)

	else:
		for i in range(len(istr)):
			if i not in cr_pm[:ind]:
				cr_pm[ind] = i
				perm(istr,ind+1)



cr_set = [-1]*4
def print_set(istr):
	p_str = []
	for i in cr_set:
		p_str.append(i)

	print(p_str)



def sets(istr,ind):

	if ind == len(istr):
		print_set(istr)

	else:
		cr_set[ind] = True
		sets(istr,ind+1)
		cr_set[ind] = False
		sets(istr,ind+1)




print(sets('abcd',0))
#print(perm('abcd',0))






# T = int(input())
# for i in range(T):
# 	N = int(input())
# 	#print(N)
# 	nums  = [int(x) for x in input().split()]
# 	mem = {}
# 	#ans = amath(nums,0,len(nums)-1)
# 	ans = amath_ita(nums)
# 	out = "Case #%s: %s"%(i+1,ans)
# 	print(out)
# 	#break
