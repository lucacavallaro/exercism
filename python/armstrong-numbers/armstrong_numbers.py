def is_armstrong_number(number):
    digits = str(number)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == number
