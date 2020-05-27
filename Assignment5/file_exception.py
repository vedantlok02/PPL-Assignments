try:
    f = open('file_name.txt')
except IOError as error: #Raised when an input/ output operation fails
    print(error)
except FileNotFoundError as fnf: #Raised when file at given path doesnt exist
	print(fnf)
except Exception as error: # General Error
    print(error)
else:
    print(f.read())
    f.close()
finally:
    print("This always works !!")