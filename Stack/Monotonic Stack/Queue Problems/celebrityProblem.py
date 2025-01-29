'''Given a square matrix mat[][] of size n x n, such that mat[i][j] = 1 means ith person knows jth person, the task is to find the celebrity. A celebrity is a person who is known to all but does not know anyone. Return the index of the celebrity, if there is no celebrity return -1.

Note: Follow 0 based indexing and M[i][i] will always be 0.

Examples:  

Input: mat = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}, {0, 0, 1, 0} }
Output: id = 2
Explanation: The person with ID 2 does not know anyone but everyone knows him


Input: mat = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 1, 0, 0}, {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.

https://www.geeksforgeeks.org/the-celebrity-problem/ '''

# Optimized approach to find the celebrity
# in the given Matrix using two-pointer approach


def celebrity(matrix, n):
    # This function returns the celebrity
    # index 0-based (if any)

    i, j = 0, n - 1
    while i < j:
        if matrix[j][i] == 1:  # j knows i
            j -= 1
        else:  # j doesn't know i so i can't be celebrity
            i += 1

    # i points to our celebrity candidate
    candidate = i

    # Now, all that is left is to check that whether
    # the candidate is actually a celebrity i.e: he is
    # known by everyone but he knows no one
    for i in range(n):
        if i != candidate:
            if matrix[i][candidate] == 0 or matrix[candidate][i] == 1:
                return -1

    # if we reach here this means that the candidate
    # is really a celebrity
    return candidate



# python program to find celebrity using
# stack data structure


def knows(a, b, matrix):
    return matrix[a][b] == 1

# Returns -1 if celebrity is not present. If present, returns id (value from 0 to n-1).


def findCelebrity(n, matrix):
    stack = []
    # Celebrity
    C = -1

    # Push everybody to stack
    for i in range(n):
        stack.append(i)

    # Extract top 2

    # Find a potential celebrity
    while len(stack) > 1:
        A = stack.pop()
        B = stack.pop()
        if knows(A, B, matrix):
            stack.append(B)
        else:
            stack.append(A)

    # Potential candidate?
    C = stack.pop()

    # Check if C is actually a celebrity or not
    for i in range(n):
        # If any person doesn't know 'C' or 'C' doesn't know any person, return -1
        if i != C and (knows(C, i, matrix) or not knows(i, C, matrix)):
            return -1

    return C



