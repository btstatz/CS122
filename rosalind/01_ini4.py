with open('rosalind_ini4.txt', 'r') as f:
	a, b = f.readline().split()
sum = 0

for x in range(int(a),int(b)+1):
	if (x % 2 == 1):
		sum = sum + x
print(sum)