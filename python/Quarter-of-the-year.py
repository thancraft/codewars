def quarter_of(month):
    if month == 1 or month == 2 or month == 3:
        return 1
    if month == 4 or month == 5 or month == 6:
        return 2
    if month == 7 or month == 8 or month == 9:
        return 3
    if month == 10 or month == 11 or month == 12:
        return 4

## Best Practices ##
# 1. 
import math

def quarter_of(month):
    return math.ceil(month/3)
    pass

# 2.
def quarter_of(month):
    if month in range(1, 4):
        return 1
    if month in range(4, 7):
        return 2
    if month in range(7, 10):
        return 3
    if month in range(10, 13):
        return 4
    

