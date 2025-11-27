def square_sum(numbers):
    if len(numbers) != 0:
        return sum([x ** 2 for x in numbers])
    if len(numbers) == 0:
        return 0

## Best Practices ##
# 1. 
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

# 2.
def square_sum(numbers):
    return sum(x * x for x in numbers) 

# 3.
def square_sum(numbers):
	res = 0
	for num in numbers:
   		res = res + num*num
	return res