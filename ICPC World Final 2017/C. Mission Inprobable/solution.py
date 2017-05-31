

def getMaxElementsRows(r,c,rows):
	max_rows = {}
	for i in range(r):
		max_rows[i] = [0,]
		for j in range(1,c):
			if rows[i][max_rows[i][0]] < rows[i][j]:
				max_rows[i] = [j,]
			elif rows[i][max_rows[i][0]] == rows[i][j]:
				max_rows[i].append(j)

	return max_rows


def getMaxElementsColumns(r,c,rows):
	max_columns = {}
	for i in range(c):
		max_columns[i] = [0,]
		for j in range(1,r):
			if rows[max_columns[i][0]][i] < rows[j][i]:
				max_columns[i] = [j,]
			elif rows[max_columns[i][0]][i] == rows[j][i]:
				max_columns[i].append(j)

	return max_columns


def reduceToOne(max_rows,max_columns,rows,i,j):
	#print(i,j)

	if rows[i][j] <= 1:
		return 0

	#print(">",i,max_rows[i],j,max_columns[j])

	if i in max_columns[j]:
		max_columns[j].remove(i)

	if j in max_rows[i]:
		max_rows[i].remove(j)

	#print(i,max_rows[i],j,max_columns[j])

	rt = rows[i][j]
	rows[i][j] = 1
	return rt - 1


def isMaxByRowUnique(max_rows,i,j,pi):
	#print(pi,i,j,max_rows[pi])
	if j in max_rows[pi] and len(max_rows[pi]) == 1:
		#print(pi,i,j,max_rows[pi])
		return True
	return False

def isMaxByColumnUnique(max_columns,i,j,pj):
	#print(pj,i,j,max_columns[j])
	if i in max_columns[pj] and len(max_columns[pj]) == 1:
		#print(pj,i,j,max_columns[j])
		return True
	return False

def gainAFixPointByColumn(r,c,max_rows,max_columns,rows,i,j):
	gain = 0
	for pj in range(c):
		if pj != j and isMaxByColumnUnique(max_columns,i,j,pj) == False:
			gain+= reduceToOne(max_rows,max_columns,rows,i,pj) 
	return gain

def gainAFixPointByRow(r,c,max_rows,max_columns,rows,i,j):
	gain = 0
	for pi in range(r):
		if pi != i and isMaxByRowUnique(max_rows,i,j,pi) == False:
			gain+= reduceToOne(max_rows,max_columns,rows,pi,j)
	return gain

def loadFixPoint(max_rows,max_columns,rows,i,j):
	loss = rows[i][max_rows[i][0]] - rows[i][j]
	if j not in max_rows[i]:
		max_rows[i].append(j)
	if i not in max_columns[j]:
		max_columns[j].append(i)
	rows[i][j] = rows[i][max_rows[i][0]]
	#print(loss)
	return loss

def gainAFixPoint(r,c,max_rows,max_columns,rows,i,j):
	gain = 0
	gain-=loadFixPoint(max_rows,max_columns,rows,i,j)
	gain+=gainAFixPointByColumn(r,c,max_rows,max_columns,rows,i,j)
	gain+=gainAFixPointByRow(r,c,max_rows,max_columns,rows,i,j)

	return gain


def fixCrossRowColumn(r,c,max_rows,max_columns,rows):
	#fix_points = []
	gain = 0
	for i in range(r):
		for j in range(c):
			if rows[i][j] > 0 and  rows[i][max_rows[i][0]] > 1 and rows[i][max_rows[i][0]] == rows[max_columns[j][0]][j]:
				#print(i,j)
				#fix_points.append((i,j))
				gain+=gainAFixPoint(r,c,max_rows,max_columns,rows,i,j)
	return gain

def gainByGeneral(r,c,max_rows,max_columns,rows):
	gain = 0
	for i in range(r):
		for j in range(c):
			if i in max_columns[j] and j in max_rows[i]:
				pass
			elif i in max_columns[j]:
				if len(max_columns[j]) > 1:
					pass
			elif j in max_rows[i]:
				if len(max_rows[i]) > 1:
					pass
			else:
				gain+= reduceToOne(max_rows,max_columns,rows,i,j)

	return gain

def getAns(r,c,rows):
	max_rows = getMaxElementsRows(r,c,rows)
	max_columns = getMaxElementsColumns(r,c,rows)
	#print(max_rows)
	#print(max_columns)
	gain = fixCrossRowColumn(r,c,max_rows,max_columns,rows)
	gain+=gainByGeneral(r,c,max_rows,max_columns,rows)
	#show_table(r,c,rows)

	return gain

def show_table(r,c,rows):
	for i in range(r):
		print(rows[i])


def main():
	while True:
		try:
			r,c  =  [int(x) for x in input().split()]
		except:
			break
		rows = {}
		for j in range(r):
			rows[j] = [int(x) for x in input().split()]

		ans = getAns(r,c,rows)
		out = "%s"%(ans,)
		#print(out)
		print(ans)



if __name__ == "__main__":
    main()