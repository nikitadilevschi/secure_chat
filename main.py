# # # Bubble sort in Python
# #
# # def bubbleSort(array):
# #     # loop to access each array element
# #     for i in range(len(array)):
# #
# #         # loop to compare array elements
# #         for j in range(0, len(array) - i - 1):
# #
# #             # compare two adjacent elements
# #             # change > to < to sort in descending order
# #             if array[j] > array[j + 1]:
# #                 # swapping elements if elements
# #                 # are not in the intended order
# #                 temp = array[j]
# #                 array[j] = array[j + 1]
# #                 array[j + 1] = temp
# #
# #
# # data = list(map(int,input("Enter the numbers:").split()))
# # print(data)
# # bubbleSort(data)
# #
# # print('Sorted Array in Ascending Order:')
# # print(data)
#
# # Python Program to check whether given sudoku board is valid
#
# # Checks for duplicates in the current row
# def validRow(mat, row):
#     # Visited array to track occurrences
#     vis = [0] * 10
#
#     for i in range(9):
#
#         # If the cell is not empty
#         if mat[row][i] != 0:
#             val = mat[row][i]
#
#             # If duplicate is found
#             if vis[val] != 0:
#                 return False
#
#             # Mark the number as visited
#             vis[val] += 1
#     return True
#
#
# # Checks for duplicates in the current column
# def colValid(mat, col):
#     # Visited array to track occurrences
#     vis = [0] * 10
#
#     for i in range(9):
#
#         # If the cell is not empty
#         if mat[i][col] != 0:
#             val = mat[i][col]
#
#             # If duplicate is found
#             if vis[val] != 0:
#                 return False
#
#             # Mark the number as visited
#             vis[val] += 1
#     return True
#
#
# # Checks for duplicates in the current 3x3 submatrix
# def subMatValid(mat, startRow, startCol):
#     # Visited array to track occurrences
#     vis = [0] * 10
#
#     for row in range(3):
#         for col in range(3):
#
#             # Current element in the submatrix
#             curr = mat[row + startRow][col + startCol]
#
#             # If the cell is not empty
#             if curr != 0:
#
#                 # If duplicate is found
#                 if vis[curr] != 0:
#                     return False
#
#                 # Mark the number as visited
#                 vis[curr] += 1
#     return True
#
#
# # Validates the Sudoku board
# def isValid(mat):
#     for i in range(9):
#         for j in range(9):
#
#             # Check if the row, column, or submatrix is invalid
#             if not validRow(mat, i) or not colValid(mat, j) or \
#                     not subMatValid(mat, i - i % 3, j - j % 3):
#                 return False
#     return True
#
#
# # Driver code
# mat = [
#     [9, 3, 0, 0, 7, 0, 0, 0, 0],
#     [1, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 5, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 4, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# print("true" if isValid(mat) else "false")


## RLE

# Function to perform Run-Length Encoding
# def run_length_encoding(input_string):
#     # Initialize an empty result string
#     result = ""
#     # Initialize the count of consecutive characters
#     count = 1
#
#     # Loop through the input string
#     for i in range(1, len(input_string)):
#         # If the current character is the same as the previous one
#         if input_string[i] == input_string[i - 1]:
#             # Increment the count
#             count += 1
#         else:
#             # Append the previous character and its count to the result
#             result += input_string[i - 1] + str(count)
#             # Reset the count
#             count = 1
#
#     # Append the last character and its count
#     result += input_string[-1] + str(count)
#
#     return result
#
#
# # Example usage
# input_string = input("write text:")
# compressed_string = run_length_encoding(input_string)
# print("Compressed string:", compressed_string)


# n = 0
# while True:
#     print("Executing While Loop")
#     if n == 5:
#         break
#     n = n + 1
# print("Finished the while loop")




########################################## WEEK 5 ###################################################

# Sample code illustrating secure password handling

import bcrypt, secrets, os


password = b"mysecretpassword"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed) # Storing hashed password instead of plaintext

# Sample code f securely generating random numbers
secure_random = secrets.token_hex(16) # Generates a secure random token
print(secure_random)

# Sample code for input validation

def validate_input(user_input):
    if not isinstance(user_input, str) or len(user_input) > 100:
        raise ValueError("Invalid input")
    user_input = input("Enter a message:")
    return user_input


# Sample code showing principle of least privilege

def delete_file(filename):
    if os.access(filename, os.W_OK):
        os. remove (filename)

filename = input("Enter the filename")