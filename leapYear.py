# A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400

# NOTE: If x%2 ==0 (has a remainder of 0), then the x is equally devisable

def is_divisible(v: int, d:int)-> bool:
    return bool(v%d)

def is_leapyear_bad(year):
    # Heavy nesting behaviour is not ideal and can be avoided in this case. (Against standard coding style guidelines)
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Pretty good as it is structured well (no heavy nesting), but is less 'pythonic' that the best option
def is_leapyear_pretty_good(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# Best option as it is structured well, and also uses the python 'truthy' idea
def is_leapyear_heaps_good(year):
    # Since ints are 'truthy' values, they can be used as a bool. If the int==0, it is treated as false, and any other number would be treated as true
    if not year % 400:
        return True
    if not year % 100:
        return False
    if not year % 4:
        return True
    return False




