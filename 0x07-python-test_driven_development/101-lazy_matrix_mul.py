#!/usr/bin/python3

import numpy as np

"""
definition of a lazy matrix function
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Resulting matrix.
    """

    try:
        # Convert input matrices to NumPy arrays
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)

        # Perform matrix multiplication using NumPy's dot function
        result = np.dot(np_m_a, np_m_b)

        return result.tolist()  # Convert NumPy array back to a Python list

    except ValueError:
        raise ValueError("shapes (n, m) and (m, p) not aligned")

    except Exception:
        raise ValueError("Failed to perform matrix multiplication")
