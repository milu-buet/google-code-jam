#Author milu


def getFreeNeighbour(pmap,pos,R,C,visited):
	neighbours = []
	i, j = pos
	RB = R - 1
	CB = C - 1

	comb4 = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

	for comb in comb4:
		x,y = comb
		if x >= 0 and x < RB and y >=0 and  y < CB and (x,y) not in visited and pmap[x][y] != '#':
			neighbours.append((x,y))

	return neighbours



def getCharPos(pmap,char,R,C):
	for i in range(R):
			if char in pmap[i]:
				return i,pmap[i].index(char)

def getSourcePos(pmap,R,C):
	return getCharPos(pmap,'S',R,C)

def getFinishPos(pmap,R,C):
	return getCharPos(pmap,'F',R,C)



def getShortestPath(pmap,R,C,S,F,visited):

	#print(S)
	if S == F:
		return 0

	visited[S] = True

	minpath = None
	for neighbour in getFreeNeighbour(pmap,S,R,C,visited):
		path = getShortestPath(pmap,R,C,neighbour,F,visited)
		#print("path>",path)
		if path is not None :
			#print("path>",path)
			if minpath:
				minpath = min(minpath,path)
			else:
				minpath = path

	if minpath is not None:
		return 1 + minpath

	return None



def isRemovable(pmap,pos):
	i,j = pos

	if pmap[i][j]!='#':
		return False

	A1 = pmap[i+1][j] == '#' and  pmap[i][j+1] == '#' and pmap[i+1][j+1] != '#'
	A2 = pmap[i-1][j] == '#' and  pmap[i][j+1] == '#' and pmap[i-1][j+1] != '#'
	A3 = pmap[i-1][j] == '#' and  pmap[i][j-1] == '#' and pmap[i-1][j-1] != '#'
	A4 = pmap[i+1][j] == '#' and  pmap[i][j-1] == '#' and pmap[i+1][j-1] != '#'

	if A1 or A2 or A3 or A4:
		return False


	return True


def getAllRemovable(pmap,R,C):
	removable = []
	for i in range(1,R-1):
		for j in range(1,C-1):
			if isRemovable(pmap,(i,j)):
				#print(i,j)
				removable.append((i,j))
				
	return removable



def getPath(R,C,D,pmap):

	#print(pmap)
	
	S = getSourcePos(pmap,R,C)
	F = getFinishPos(pmap,R,C)
	visited = {}
	dist = getShortestPath(pmap,R,C,S,F,visited)
	tryAllRemove(pmap,R,C)

	if dist <= D:
		return 'POSSIBLE'

	return dist



def showmap(pmap):
	for line in pmap:
		print(line)

'''
##########
#S#...#.F#
#...#...##
##########

'''

T = int(input())
for i in range(T):
	R,C,D  = [int(x) for x in input().split()]
	pmap = []
	for j in range(R):
		pmap.append(input())
	ans = getPath(R,C,D,pmap)
	out = "Case #%s: %s"%(i+1,ans)
	print(out)
	showmap(pmap)