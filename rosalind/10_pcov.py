with open('rosalind_pcov.txt','r') as f:
	reads = [read.strip() for read in f.readlines()]

dict = {}
for kmer_a in reads:
	for kmer_b in reads:
		if kmer_a[1:] == kmer_b[:-1]:
			dict[kmer_a] = kmer_b

seq = ''
current_key = dict.keys()[0]
for i in range(len(dict.keys())):
	seq += current_key[0]
	current_key = dict[current_key]
	
print seq