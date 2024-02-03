def numeric_sort_slow(list_A):
    ### incidenec matrix based implimentaion
	list_B = [ [0]*len(list_A) for _ in list_A ]  # create a matrix with zero element
	
	for row,i in enumerate(list_B):
		for column,j in enumerate(i):
			if(list_A[row] > list_A[column]):
				list_B[row][column] = 1
	list_C = [ sum(i) for i in list_B ]
	list_S = [ 0 for i in list_A ]
	for x,y in enumerate(list_C):
		list_S[y] = list_A[x]
	for x, y in enumerate(list_S):
		if x != 0 and list_S[x] == 0 and list_S[x-1] != 0:
			list_S[x] = list_S[x-1]
	return list_S
    
def numeric_sort_fast(list_A):
    ### non incidenece matrix based implementation
	my_dict = {}
	for x, y in enumerate(list_A):
		my_dict[x] = sum((1 if y > row else 0 for row in (list_A)))   #  coverted list comprehension to generator
	list_S = [ 0 for i in list_A ]
	for key in my_dict.keys():
		list_S[my_dict[key]] = list_A[key]
	for x, y in enumerate(list_S):
		if x != 0 and list_S[x] == 0 and list_S[x-1] != 0:
			list_S[x] = list_S[x-1]
	return list_S

def factorial(n):
    # recursive fuction to calculate factorial of a given number
	return 1 if (n==1 or n==0) else n * factorial(n - 1)


if __name__ == "__main__":
	A = [22, 40, 22, 22, 100, 0, 23,  99, 22, 1000, 1000,  700, 40, 2, 1, 11, 5, 9, 22]
	#A = []
	#A = [ i for i in range(30000)]
	#A[1] = 5
	S = numeric_sort_fast(A)
	print(S)

