# def permutations(string):
#     count_str = len(string)
#     loop = 0


# permutations('aabb')

# Python program to print all permutations using
# Heap's algorithm
 
# Prints the array
 
 
def printArr(a, n):
    for i in range(n):
        print(a[i], end=" ")
    print()
 
# Generating permutation using Heap Algorithm
 
 
def heapPermutation(a, size, n):
 
    # if size becomes 1 then prints the obtained
    # permutation
    if (size == 1):
        printArr(a, n)
        return
 
    for i in range(size):
        if (size == 1):
            printArr(a, n)
            return
        
        for i in range(size):
            if (size == 1):
                printArr(a, n)
                return
        
            for i in range(size):
                heapPermutation(a, size-1, n)
        
                # if size is odd, swap 0th i.e (first) 
                # and (size-1)th i.e (last) element
                # else If size is even, swap ith 
                # and (size-1)th i.e (last) element
                if size & 1:
                    a[0], a[size-1] = a[size-1], a[0]
                else:
                    a[i], a[size-1] = a[size-1], a[i]
    
            # if size is odd, swap 0th i.e (first) 
            # and (size-1)th i.e (last) element
            # else If size is even, swap ith 
            # and (size-1)th i.e (last) element
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]
 
        # if size is odd, swap 0th i.e (first) 
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith 
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
 
 
# Driver code
a = [char for char in "aabb"]
n = len(a)
heapPermutation(a, n, n)
 
# This code is contributed by ankush_953