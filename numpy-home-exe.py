import numpy as np
np.random.seed(42)

if __name__ == '__main__':
    ###
    # Exercise 1:

    np_random_array = np.random.randint(10, 99, (4, 3))
    print(np_random_array)

    print(f"Sum of all elements: {np_random_array.sum()}")
    print(f"Sum of each row : {np_random_array.sum(axis=1)}")
    print(f"Sum of each column : {np_random_array.sum(axis=0)}")

    ###
    # Exercise 2:
    random_array = np.random.randint(0, 11, 10)
    print(random_array)
    even = random_array % 2 == 0
    print(f"The amount of even numbers is {even.sum()}")

    ###
    # Exercise 3:

    np_array = np.arange(0, 100)
    print(f"1'\n")
    print(np_array, "\n")
    print(f"2'\n")
    reshape_array = np_array.reshape(10, 10)
    print(reshape_array, "\n")
    print(f"3'\n")
    reshape_array[reshape_array > 50] = -1
    print(reshape_array, "\n")
    print(f"4'\n")
    print(f"Sum of all elements in the array : {reshape_array.sum()},\n")
    print(f"5'\n")
    print(f"Mean of all elements in the array : {reshape_array.mean()}")
    ###
    # Exercise 4:
    lin_array = np.linspace(0, 100, 10)
    print(f'First array : {lin_array}')
    new_lin_array = lin_array[(lin_array > 50) | (lin_array < 20)].copy()
    print(f"New array : {new_lin_array} ")


    def array_dreshaped(new_lin_array):
        try:
            new_lin_array = new_lin_array.reshape(2, -1)
        except ValueError:
            print(f"not possible to reshape a array whit : {new_lin_array.size} elements ")


    array_dreshaped(new_lin_array)

    ###
    # Exercise 5:
    np_zeros = np.zeros((4,4),dtype= int)
    print(np_zeros)


    def change_values_random(matrix):
        indexes = [(0, 0), (3, 3)]
        matrix[1:3, 1] = np.random.randint(10, 101, size=(1,2))
        matrix[1:3, 2] = np.random.randint(10, 101, size=(1,2))
        for row, col in indexes:
            np_zeros[row,col] = np.random.randint(10,101)
        return np_zeros

    change_values_random(np_zeros)