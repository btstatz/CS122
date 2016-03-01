dict = {}
with open('rosalind_ini6.txt', 'r') as f:
	for line in f:
		for word in line.split():
			if word in dict:
				dict[word] += 1
			else:
				dict[word] = 1

for item in dict:
	print item, dict[item]