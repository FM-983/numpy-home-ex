import numpy as np
np.random.seed(42)

if __name__ == '__main__':
    ###
    print("Exercise 1:\n")
    ###

    np_random_array = np.random.randint(10, 99, (4, 3))
    print(np_random_array)
    sum_array = np_random_array.sum()
    print(f"Sum of all elements: {sum_array}\n")
    row_sum = np_random_array.sum(axis=1)
    print(f"Sum of each row : {row_sum}\n")
    column_sum = np_random_array.sum(axis=0)
    print(f"Sum of each column : {column_sum}")

    ###
    print("\nExercise 2:\n")
    ###

    random_array = np.random.randint(0, 11, 10)
    print(random_array)
    even = random_array % 2 == 0
    print(f"The amount of even numbers is {even.sum()}")

    ###
    print("\nExercise 3:\n")
    ###

    np_array = np.arange(0, 100)
    print(f"*'\n")
    print(np_array, "\n")
    print(f"**'\n")
    reshape_array = np_array.reshape(10, 10)
    print(reshape_array, "\n")
    print(f"***'\n")
    reshape_array[reshape_array > 50] = -1
    print(reshape_array, "\n")
    print(f"****'\n")
    print(f"Sum of all elements in the array : {reshape_array.sum()},\n")
    print(f"*****'\n")
    print(f"Mean of all elements in the array : {reshape_array.mean()}")

    ###
    print("\nExercise 4:\n")
    ###

    lin_array = np.linspace(0, 100, 10)
    print(f'First array : {lin_array}')
    new_lin_array = lin_array[(lin_array > 50) | (lin_array < 20)].copy()
    print(f"New array : {new_lin_array} ")


    def array_dreshaped(new_lin_array):
        try:
            new_lin_array = new_lin_array.reshape(2, -1)
            print(new_lin_array)
        except ValueError:
            print(f"not possible to reshape a array whit : {new_lin_array.size} elements ")


    array_dreshaped(new_lin_array)

    ###
    print("\nExercise 5\n")
    ###

    np_zeros = np.zeros((4, 4), dtype=int)
    print(np_zeros)


    def change_values_random(matrix):
        rows, cols = matrix.shape
        random_value = lambda: np.random.randint(10, 101)

        matrix[0, 0] = random_value()

        matrix[rows - 1, cols - 1] = random_value()

        center_x, center_y = rows // 2, cols // 2
        matrix[center_x, center_y] = random_value()

        return matrix

    print(f"Solution example : \n {change_values_random(np_zeros)}")



