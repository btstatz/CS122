indices = []
with open('rosalind_subs.txt', 'r') as f:
	str1 = f.readline().rstrip()
	str2 = f.readline().rstrip()
	for i in range(len(str1) - len(str2)):
		if str1[i:i+len(str2)] == str2:
			indices.append(i+1)

for x in indices:
	print(x)