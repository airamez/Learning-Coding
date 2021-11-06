# Using a tuple to return values from a function


def integer_division(dividend: int, divisor: int) -> ():
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


division = integer_division(7, 3)
print(type(division))
print("7 // 4 => Quotient =", division[0], "Remainder =", division[1])
