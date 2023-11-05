#!/usr/bin/python3
def add_tuples(tuple_a=(), tuple_b=()):
    # Initialize an empty list to store the result values
    result = []

    # Loop through indices 0 and 1 (for a 2-element tuple)
    for i in range(2):
        # If length of tuple_a is greater than the current index (i),
        # take value from tuple_a at that index, otherwise, use 0.
        a_value = tuple_a[i] if len(tuple_a) > i else 0

        # If length of tuple_b is greater than the current index (i),
        # take value from tuple_b at that index, otherwise, use 0.
        b_value = tuple_b[i] if len(tuple_b) > i else 0

        # Add values from tuple_a and tuple_b and append the result to the list
        result.append(a_value + b_value)

    # Convert the list of result values into a tuple and return it
    return tuple(result)
