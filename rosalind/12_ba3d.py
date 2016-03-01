with open('rosalind_ba3d.txt','r') as f:
	kmer_length = int(f.readline().strip())
	seq = f.readline().strip()

dict = {}
for offset in range(len(seq)-kmer_length+1):
	prefix = seq[offset:offset+kmer_length-1]
	suffix = seq[offset+1:offset+kmer_length]
	if prefix in dict:
		dict[prefix].append(suffix)
	else:
		dict[prefix] = [suffix]

for key in sorted(dict):
	print(key + " -> " + ','.join(sorted(dict[key])))