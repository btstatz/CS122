with open('rosalind_ba3e.txt','r') as f:
	reads = [read.strip() for read in f.readlines()]

dict = {}
for read in reads:
	prefix = read[:-1]
	suffix = read[1:]
	if prefix in dict:
		dict[prefix].append(suffix)
	else:
		dict[prefix] = [suffix]

for key in sorted(dict):
	print(key + " -> " + ','.join(sorted(dict[key])))