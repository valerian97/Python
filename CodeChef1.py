tests = int(input(''))
results = [True for i in range(tests)]
for i in range(tests):
	n = int(input(''))
	#x = input('')
	#x = x.split(' ')
	num = list(map(int, input().split()))
	#for i in range(n):
	#	num.append(int(input('')))
	sets = [( num[i], num[j]) for i in range(len(num)) for j in range(len(num)) if j != i]
	for item in sets:
		prod = item[0]*item[1]
		if prod not in num:
			results[i] = False
			break
for i in results:
	if i == True:
		print('yes')
	else:
		print('no')
