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


def getDist(pos1,pos2):
	x1,y1 = pos1
	x2,y2 = pos2
	return (x1-x2)**2 + (y1-y2)**2

def getIntelNeighbour(pmap,pos,R,C,F,visited):

	neighbours = []
	i, j = pos
	RB = R - 1
	CB = C - 1

	comb4 = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

	for comb in comb4:
		x,y = comb
		if x > 0 and x < RB and y >0 and  y < CB and (x,y) not in visited:
			neighbours.append((x,y,getDist(comb,F))) 


	neighbours.sort(key=lambda x: x[2])

	#print(neighbours)
	return neighbours



def getCharPos(pmap,char,R,C):
	for i in range(R):
			if char in pmap[i]:
				return i,pmap[i].index(char)

def getSourcePos(pmap,R,C):
	return getCharPos(pmap,'S',R,C)

def getFinishPos(pmap,R,C):
	return getCharPos(pmap,'F',R,C)



def getShortestPath(pmap,R,C,D,S,F,visited,pstep):

	#print(S,F)
	if S == F:
		return 0

	if pstep > D:
		return None

	visited[S] = True

	minpath = None
	#for neighbour in getFreeNeighbour(pmap,S,R,C,visited):
	for neighbour in getIntelNeighbour(pmap,S,R,C,F,visited):
		i,j = S_ = neighbour[0],neighbour[1]
		if S_ not in visited:
			path = None
			saved = None
			if pmap[i][j] == '#' and isRemovable(pmap,S_):
				saved = pmap[i] 
				pmap[i] = pmap[i][0:j] + '.' + pmap[i][j+1:] 
				path = getShortestPath(pmap,R,C,D,S_,F,visited,pstep + 1)

			elif pmap[i][j] != '#':
				path = getShortestPath(pmap,R,C,D,S_,F,visited,pstep + 1)

			if path is not None :
				#print("path>",path)
				if minpath:
					minpath = min(minpath,path)
				else:
					minpath = path
			elif saved:
				pass
				pmap[i] = saved

	if minpath is not None:
		if minpath + 1 >  D:
			return None

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

	dx = [-1, 0, 1, 0, 1, 1, -1, -1]
	dy = [0, 1, 0, -1, 1, -1, 1, -1]

	cnt = 0
	h = 0
	for q in range(4):
		xk = i + dx[q]
		yk = j + dy[q]
		if pmap[xk][yk] == '#':
			cnt+=1
			h ^= q   

	if cnt == 0 or cnt == 1 or (cnt == 2 and (h & 1)):
		return True


	return False


def getAllRemovable(pmap,R,C):
	removable = []
	for i in range(1,R-1):
		for j in range(1,C-1):
			if isRemovable(pmap,(i,j)):
				#print(i,j)
				removable.append((i,j))
				
	return removable


def tryAllRemove(pmap,R,C,D,S,F):

	visited = {}
	dist = getShortestPath(pmap,R,C,D,S,F,visited,0)

	if dist and dist <= D:
		return 'POSSIBLE'

	# all_removable = getAllRemovable(pmap,R,C)
	# #print(all_removable)

	# for removable in getAllRemovable(pmap,R,C):
	# 		i,j = removable
	# 		saved = pmap[i]
	# 		pmap[i] = pmap[i][0:j] + '.' + pmap[i][j+1:] 
	# 		if tryAllRemove(pmap,R,C,D,S,F) == 'POSSIBLE':
	# 			return 'POSSIBLE'

	# 		pmap[i] = saved

	#return dist
	return 'IMPOSSIBLE'


def getPath(R,C,D,pmap):

	S = getSourcePos(pmap,R,C)
	F = getFinishPos(pmap,R,C)
	return tryAllRemove(pmap,R,C,D,S,F)



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
	if ans == 'POSSIBLE':
		showmap(pmap)