import numpy as np

"""
Testing the argmax function in response to randomly generated arrays
"""

def print_random_test(samples):
    for i in range(10):
        randoms = np.random.normal(0, 1, samples)
        print(randoms)
        print(np.argmax(randoms))

"""Test """
print_random_test(5)