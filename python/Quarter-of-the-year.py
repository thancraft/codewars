# import math

# def quarter_of(month):
#     return math.ceil(month/3)

def quarter_of(month):
    if month in range(1, 4):
        return 1
    if month in range(4, 7):
        return 2
    if month in range(7, 10):
        return 3
    if month in range(10, 13):
        return 4