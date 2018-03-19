mul_of_3 = 0
mul_of_5 = 0
for num in range(1000):
	if num% 3 == 0:
		mul_of_3 = num  
		print mul_of_3
	elif num % 5 == 0:
		mul_of_5 = num
		print mul_of_5
