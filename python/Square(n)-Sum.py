def square_sum(numbers):
    if len(numbers) != 0:
        return sum([x ** 2 for x in numbers])
    if len(numbers) == 0:
        return 0

## Best Practices ##

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


