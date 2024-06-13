import math


def unitCut(n):
    # Find the closest number to x that is a power of two

    # Calculate the logarithm of x to the base 2
    log_base_two = math.log2(n)

    # Round the logarithm up to the next integer. Returns closest power of two to x
    closest_power_of_two = int(math.ceil(log_base_two))

    min_cuts = closest_power_of_two

    # First cut will be at 2 raised to min_cuts - 1
    first_cut = int(math.pow(2, min_cuts - 1))
    print("For n :", n)
    print("Minimum cuts: ", min_cuts)
    print("First Cut: ", first_cut)


unitCut(50000)
