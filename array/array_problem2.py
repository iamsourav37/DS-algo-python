# Find the occurrence of an integer in the array

import numpy as np


def main():
    array = np.array([0, 1, 12, 1, 0, 3, 0])

    # find how many zeros are there
    search_element = 0

    count = 0
    for i in range(len(array)):
        if array[i] == search_element:
            count += 1
    print(f"{search_element} occurance : {count}")


if __name__ == "__main__":
    main()
