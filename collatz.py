"""Calculate Collatz Numbers"""


def get_collatz_numbers(number=10):

    hail_numbers = []

    while(True):
        hail_numbers.append(number)

        if number == 1:
            break

        if number % 2 != 0:
            number = (number * 3) + 1
        else:
            number = number / 2

    return hail_numbers
