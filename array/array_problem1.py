# Write a program to reverse the array

import numpy as np


def main():


    size_of_array = 5
    array = np.zeros(size_of_array, dtype=int)
    for i in range(size_of_array):
        array[i] = int(input("Enter value : "))

    print(f"Before reversing the array : {array}")

    # reversing the array
    for i in range(size_of_array//2):
        array[i], array[size_of_array-1-i] = array[size_of_array-1-i], array[i]

    print(f"After reversing the array : {array}")


if __name__ == "__main__":
    main()

