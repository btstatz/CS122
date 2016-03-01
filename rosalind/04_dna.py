dict = {}
with open('rosalind_dna.txt', 'r') as f:
	for line in f:
		for x in range(len(line)):
			if line[x] in dict:
				dict[line[x]] += 1
			else:
				dict[line[x]] = 1

print dict['A'], dict['C'], dict['G'], dict['T']