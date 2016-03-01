with open('rosalind_ini5.txt', 'r') as f:
	index = 0
	for line in f:
		index += 1
		if index % 2 == 0:
			print(line)