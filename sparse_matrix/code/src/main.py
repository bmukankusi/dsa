import sys
import os
from spa_matrix import SparseMatrix

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <operation> <matrix_file_1> <matrix_file_2>")
        print("Operations: add, subtract, multiply")
        return

    operation = sys.argv[1]
    matrix_file_1 = sys.argv[2]
    matrix_file_2 = sys.argv[3]

    try:
        matrix1 = SparseMatrix(matrix_file_1)
        matrix2 = SparseMatrix(matrix_file_2)

        if operation == 'add':
            result = matrix1.add(matrix2)
            result_file = f"result_add_{os.path.basename(matrix_file_1).split('.')[0]}_{os.path.basename(matrix_file_2).split('.')[0]}.txt"
        elif operation == 'subtract':
            result = matrix1.subtract(matrix2)
            result_file = f"result_subtract_{os.path.basename(matrix_file_1).split('.')[0]}_{os.path.basename(matrix_file_2).split('.')[0]}.txt"
        elif operation == 'multiply':
            result = matrix1.multiply(matrix2)
            result_file = f"result_multiply_{os.path.basename(matrix_file_1).split('.')[0]}_{os.path.basename(matrix_file_2).split('.')[0]}.txt"
        else:
            print(f"Unknown operation '{operation}'. Use 'add', 'subtract', or 'multiply'.")
            return

        result.save_to_file(result_file)
        print(f"Operation completed successfully. Result saved to '{result_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
