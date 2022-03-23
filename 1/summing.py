def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(101))
    elif numbers is []:
        return 0
    else:
        return sum(numbers)
