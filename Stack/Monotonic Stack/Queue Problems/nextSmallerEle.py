'''Given a circular integer array A, return the next smaller element for every element in A. The next smaller element for 
an element x is the first element smaller than x that we come across while traversing the array in a clockwise manner. 
If it doesn't exist, return n for this element.'''

def nextSmaller(A):
    s = []
    res = []
    
    for i in range(len(A)-1,-1,-1):
        while s and A[i] <= A[s[-1]]:
            s.pop()
        if not s:
            res.append(len(A))
        else :
            res.append(s[-1])
        s.append(i)

    return res[::-1]