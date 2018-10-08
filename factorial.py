# program for find factorial in one line

print(reduce( (lambda x, y: x + y), [x for x in range(1,int(input("Enter value to find factorial: "))+1)] )) 

#	using reduce method
#	>>> reduce(aFunction, aSequence)
#	It applies a rolling computation to sequential pairs of values in a list
