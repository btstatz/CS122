import numpy as np

#Read file
str1 = ''
str2 = ''

with open('rosalind_edta.txt','r') as f:
	f.readline()
	temp = ''
	for line in f.readlines():
		if (line.strip()[0] == '>'):
			str1 = temp
			temp = ''
		else:
			temp = temp + line.strip()
	str2 = temp


#Generate matrix, save traceback pointers
matrix = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
traceback = [[[] for j in range(len(str2)+1)] for i in range(len(str1)+1)]

for i in range(len(str1)+1):
	matrix[i][0] = i
for j in range(len(str2)+1):
	matrix[0][j] = j

for j in range(1, len(str2)+1):
	for i in range(1, len(str1)+1):
		deletion = matrix[i-1][j] + 1
		insertion = matrix[i][j-1] + 1
		identity = matrix[i-1][j-1] if str1[i-1] == str2[j-1] else np.inf
		substitution = matrix[i-1][j-1] + 1 if str1[i-1] != str2[j-1] else np.inf
		
		minval = min(insertion, deletion, identity, substitution)
		matrix[i][j] = minval
		if (minval == deletion):
			(traceback[i][j]).append([i-1, j])
		if (minval == insertion):
			(traceback[i][j]).append([i, j-1])
		if (minval == identity or minval == substitution):
			(traceback[i][j]).append([i-1, j-1])

print(int(matrix[len(str1)][len(str2)]))


#Find path
out1 = ''
out2 = ''
i = len(str1)
j = len(str2)

while(i != 0 and j != 0):
	prev_i = traceback[i][j][0][0]
	prev_j = traceback[i][j][0][1]
	
	if (prev_j == j):	#insertion
		out1 = str1[prev_i] + out1
		out2 = '-' + out2
	elif (prev_i == i):	#deletion
		out1 = '-' + out1
		out2 = str2[prev_j] + out2
	else:	#identity or substitution
		out1 = str1[prev_i] + out1
		out2 = str2[prev_j] + out2
		
	i = prev_i
	j = prev_j

print(out1)
print(out2)