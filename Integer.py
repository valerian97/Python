def integers(number):
	try:
		ret = int(float(number))
	except ValueError:
		ret = 0
	return ret
print(integers("-41.42"))
