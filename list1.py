list1 = [1,2,3,4,5]
def func(iplist):
	retlist = []
	for i in range(len(iplist)):
		retlist.append(iplist.pop())
	return retlist

list2 = func(list1[:])
print(list2)
