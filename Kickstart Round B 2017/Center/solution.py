# Milu


def get_max_dist(center,point):
	return float(max(abs(center[0]-point[0]),abs(center[1]-point[1])))

def get_sum_dist(center,points):
	return sum([ get_max_dist(center,points[i]) for i in points])

def get_avg(point1,point2):
	x = (point1[0] + point2[0])/2
	y = (point1[1] + point2[1])/2

	return x,y

def get_ans(points,N):
	#s = get_max_dist(1,2,3,4)
	#print(s)
	center_x = 0.0
	center_y = 0.0
	for i in points:
		center_x+=points[i][0]
		center_y+=points[i][1]

	center = (center_x/N),(center_y/N)

	return get_sum_dist(center,points)


T = int(input())
for i in range(T):
	N = int(input())
	arr = {}
	for j in range(N):
		arr[j] = [float(x) for x in input().split()]
	ans = get_ans(arr,N)
	out = "Case #%s: %s"%(i+1,ans)
	print(out)
	#break
