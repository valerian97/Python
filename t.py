try:
    print "Performing an action which may throw an exception."
except Exception as error:
    print "An exception was thrown!"
    print str(error)
else:
    print "Everything looks great!"
finally:
    print "Finally is called directly after executing the try statement whether an exception is thrown or not."
