import numpy as np

# Find minimum and maximum element in an array



def main():
    size_of_array = 5
    array = np.zeros(size_of_array, dtype=int)

    for i in range(size_of_array):
        array[i] = int(input("Enter value : "))

    # find min and max

    min = max = array[0]

    for i in range(size_of_array):
        if min > array[i]:
            min = array[i]
        if max < array[i]:
            max = array[i]
    print(f"Minimum value : {min}. Maximum value : {max}")


if __name__ == "__main__":
    main()

