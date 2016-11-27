#Author milu

T9_dict = {
	' ':	'0',
	'abc':  '2',
	'def':  '3',
	'ghi':  '4',
	'jkl':  '5',
	'mno':  '6',
	'pqrs': '7',
	'tuv':  '8',	
	'wxyz':  '9',
}

def getT9(words):

	ans = []
	t9 = None
	pre_key = None
	for char in words:
		for key in T9_dict.keys():
			if char in key:
				pos = key.index(char) +1
				if pre_key and pre_key == T9_dict[key]:
					ans.append(" ")
				t9 = T9_dict[key]*pos
				pre_key = T9_dict[key]
				ans.append(t9)

	return "".join(ans)


N = int(input())
for i in range(N):
	words  = input()
	ans = getT9(words)
	out = "Case #%s: %s"%(i+1,ans)
	print(out)