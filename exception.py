def faculty():
	raise Exception('Something is wrong!')
	
def ignore_exception():
	faculty()
	
def handle_exception():
	try:
		faculty()
	except:
		print('Exception Handled!')
handle_exception()
ignore_exception()
