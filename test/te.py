#print 'run...'

mem = {}

def amath(arr,i,j):
	if i >= j or (i,j) in mem: 
		return 0

	mem[i,j] = True
	print (arr[i],arr[j])

	A = (arr[j]-arr[i])*(2**(j-i-1))
	B = amath(arr,i+1,j)
	C = amath(arr,i,j-1)

	return (A+B+C)

def amath_ita(arr):

	summ = 0
	L = len(arr) - 1
	for i in range(L+1):
		rsum = 0
		for j in range(L,i,-1):
			rsum = ((arr[j]-arr[i]) + rsum*2)%1000000007
		summ= (summ + rsum)%1000000007

	return summ


# arr = [3,6,7,9]
# arr = [2181, 2947, 3310, 3796, 5043, 6110, 6727, 8088, 8554, 9257]
# result = amath(arr,0,len(arr)-1)
# print result%1000000007

T = int(input())
for i in range(T):
	N = int(input())
	#print(N)
	nums  = [int(x) for x in input().split()]
	mem = {}
	#ans = amath(nums,0,len(nums)-1)
	ans = amath_ita(nums)
	out = "Case #%s: %s"%(i+1,ans)
	print(out)
	#break
