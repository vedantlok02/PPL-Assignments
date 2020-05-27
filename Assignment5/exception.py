try:
	a = int (input ())
	b = int (input ())
	c =  a/b
	print (c)	#if we divide by 0, program fails.

except ZeroDivisionError as zero:
	print (zero)

except Exception:	# General error is used below specific errors
	print('except block runs when there\'s a problem with try. Exception is base class for all errors')

else:
	print ('else block runs when try works')

finally:
	print ('finally block always works')



