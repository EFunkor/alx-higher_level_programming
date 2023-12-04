#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """definition of the print_sorted method
    """
    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
