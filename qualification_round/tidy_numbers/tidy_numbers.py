# tidy_numbers.py

# NOTE: Attempt to scale for numbers of 10^18 (i.e., 18 digits)

def tidy_numbers(*args):

    num_str = args[0]

    # Okay to use, because 1 <= N
    last_digit = -1

    # Loop through digits
    for digit_str in num_str:
        this_digit = int(digit_str)
        if int

        last_digit = this_digit
