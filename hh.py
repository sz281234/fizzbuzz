for i in range(0,101):
	if i % 3 == 0 and not i % 5 == 0:
		print ("fizz: %d" % i)
	elif i % 5 == 0 and not i % 3 == 0:
		print ("buzz: %d" % i)
	elif i % 3 == 0 and i % 5 == 0:
		print ("FIZZBUZZ: %d" % i)
	else:
		print (i)
