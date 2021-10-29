import numpy as np


elements = np.zeros(6, dtype=int)

for i in range(len(elements)):
    elements[i] = int(input("Enter next value : "))

search_element = int(input("Enter search element : "))

for i in range(len(elements)):
    if elements[i] == search_element:
        print(f"Index of {search_element} is : {i}")
        break
else:
    print(f"{search_element} is not found")




