print(1)
def currency_converter(rate, euros):
	dollars = euros*rate
	return dollars
euros = input('Enter euros')
rate = input('Enter rate')
print('Final value: ', currency_converter(rate, euros))
