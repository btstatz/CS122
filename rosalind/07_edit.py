import numpy as np

with open('rosalind_edit.txt','r') as f:
	f.readline()
	str1 = ''
	str2 = ''
	temp = ''
	for line in f.readlines():
		if (line.strip()[0] == '>'):
			str1 = temp
			temp = ''
		else:
			temp = temp + line.strip()
	str2 = temp

if (str1 == str2):
	print(0)
if (len(str1) == 0):
	print(len(str2))
if (len(str2) == 0):
	print(len(str1))
	
matrix = np.zeros((len(str1)+1, len(str2)+1))

for i in range(len(str1)+1):
	matrix[i, 0] = i
for j in range(len(str2)+1):
	matrix[0, j] = j

for j in range(1, len(str2)+1):
	for i in range(1, len(str1)+1):
		deletion = matrix[i-1, j] + 1
		insertion = matrix[i, j-1] + 1
		identity = matrix[i-1, j-1] if str1[i-1] == str2[j-1] else np.inf
		substitution = matrix[i-1, j-1] + 1 if str1[i-1] != str2[j-1] else np.inf
		matrix[i, j] = min(insertion, deletion, identity, substitution)

print(int(matrix[len(str1), len(str2)]))