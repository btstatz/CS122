from itertools import product

dict = {''.join(i): 0 for i in product("ACGT", repeat = 4)}

with open('rosalind_kmer.txt', 'r') as f:
	f.readline()
	seq = f.read().replace("\n", "")
	for i in range(len(seq) - 3):
		subseq = seq[i:i+4]
		dict[subseq] += 1
		
for x in sorted(dict.keys()):
	print(dict[x])