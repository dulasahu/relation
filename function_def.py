import os
import socket
from itertools import permutations
import sys
import numpy

def split_square_matrix(my_mat,size):
    """
    splits a squre matrix with the size specified, 
    returns a  list containing submatrix of size * size shape
    input matrix row or column legth should be divisible by size
	ex- split_square_matrix(mat1,3)
    """
    row_len , column_len = my_mat.shape
    row_sub_len = row_len//size
    column_sub_len = column_len//size
    mat2 = numpy.vsplit(my_mat, row_sub_len)
    mat3_list = [numpy.hsplit(x, column_sub_len) for x in mat2]
    return mat3_list
	
def matrix_invariant(my_mat):
	"""
	returns list of a square matrix basic invariants
	"""
    eigen_values = numpy.linalg.eig(my_mat)
    positive_eigen_values = len([x for x in eigen_values[0] if x > 0])
    negative_eigen_values = len([x for x in eigen_values[0] if x < 0])
    rank = int(numpy.linalg.matrix_rank(my_mat))
    index = positive_eigen_values
    signature=abs(positive_eigen_values-negative_eigen_values)
    return(rank,index,signature)

def matrix_invarint_of_submatrix_list(my_list):
    """
    retruns a list of invarint of submatrix
    """
    invariant_list = [[matrix_invariant(y) for y in x] for x in my_list]
    return invariant_list

def matrix_trace(my_matrix):
    eigen_values = numpy.linalg.eigvals(my_matrix)
    trace = sum(eigen_values)
    return trace

def index_no(my_string):
    """
    calculate index number of a string
    """
    
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    my_string_list = [x for x in my_string]
    mysum = 0
    for i,x in enumerate(my_string_list):
        for j,y in enumerate(alphabet):
            if x==y:
                mysum += (j+1)*(i+1)
    return mysum

def index_no_two(my_string):
    """
    calculate index number of a string using matrix multiplication
    """	
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    alphabet_no = [[x+1] for x in range(len(alphabet))]
    my_string_list = [x for x in my_string]
    incidence = [[0]*26 for x in my_string_list]
    for i,x in enumerate(my_string_list):
        for j,y in enumerate(alphabet):
            if x==y:
                incidence[i][j] = i+1
    inci = numpy.mat(incidence)
    alph = numpy.mat(alphabet_no)
    product = inci*alph
    p1 = numpy.sum(product)
    return p1
def generate_subset_list(input_list):
    """this function can generate s subset list from  a input list by using binary counting
     bin function is used to convert to finary format , slicing used to remove 0b then rjust used for padding """
    test_len = len(input_list)
    count = 2**test_len
    subset_list = []
    for x in range(0,count,1):
        bin_value = bin(x)[2:].rjust(test_len, '0')
        subset = [ input_list[i] for i, x in enumerate(bin_value) if x == "1"]
        subset_list.append(subset)
        #yield subset
    return subset_list

def cart_product(list1,list2):
    perm = []
    for x in list1:
        for y in list2:
            if y not in x:
                my_list = [x for x in x]
                my_list.append(y)
                perm.append(my_list)
    if (len(perm[0])==len(list2)):
        return perm
    else:
        return cart_product(perm,list2) 

def perm(my_list):
    product = cart_product(my_list,my_list)
    return product



def num_square(func):
    """
    Decorator example
    """
    def wrapper():
        a = func()
        b = [x**2 for x in a]
        return b
    return wrapper

@num_square
def num_list():
    a = [1,2,3,4,5]
    return a
	
def max_bin_search(l1):
    """
    Recursive function to find the largest number from a list, used tree , left and right comparison 
    """
    if len(l1)%2 == 0:
        l1.append(l1[-1])
    for x in range(len(l1)//2):
        if l1[2*x+1] > l1[2*x+2]:
            l = l1[2*x+1]
            r = l1[2*x+2]
            l1[2*x+1] = r
            l1[2*x+2] = l

    root_right = [x for i,x in enumerate(l1) if i%2 == 0 ]

    if len(root_right) == 3:
        max = root_right[0]
        for x in root_right:
            if x > max:
                max = x
        return max
    return max_bin_search(root_right)

def min_bin_search(l1):
    """
    Recursive function to find the smallest number from a list, used tree , left and right comparison 
    """
    if len(l1)%2 == 0:
        l1.append(l1[-1])
    for x in range(len(l1)//2):
        if l1[2*x+1] > l1[2*x+2]:
            l = l1[2*x+1]
            r = l1[2*x+2]
            l1[2*x+1] = r
            l1[2*x+2] = l

    root_left = [x for i,x in enumerate(l1) if i%2 != 0 ]
    root_left.insert(0,l1[0])

    if len(root_left) == 3:
        min = root_left[0]
        for x in root_left:
            if x < min:
                min = x
        return min
    return min_bin_search(root_left)
	
def matrix_transpose(mat):
    """
    returns transpose of a matrix
    """
    transpose_mat = [ [0]*len(mat) for x in mat[0]]
    for i,x in enumerate(transpose_mat):
        for j,y in enumerate(x):
            transpose_mat[i][j] = mat[j][i]
    return transpose_mat
def matrix_multiplication(mat_1,mat_2):
    """
    Tested with smaller dimesion matrix, need to test higher dimesion matrix
    make sure  both matrix are of same dimension
    or mat_2 coloumn length is smae as mat_1 row legth
    ex-
    m1 = [[1, 2], [1, 2]]
    m2 = [[2],[2]]
    m1*m1
    m1*m2
    m3 = [[1, 2,3], [1, 2,3]]
    m4 = [[1],[2],[3]]
    m3*m4
    """
    mat_product = [[0]*len(mat_2[0]) for x in mat_1]

    for i,x in enumerate(mat_1):
        for j,y in enumerate(x):
            for z in range(len(mat_2[0])):
                mat_product[i][z] += mat_1[z][j] * mat_2[j][z]
    return mat_product


def lexical_character_sort(string_list):
    """
    sorting using cartesian product, cartesian product is inherently sorted
    """
    max_string_length = len(string_list[0])
    for x in string_list:
        if len(x) > max_string_length:
            max_string_length = len(x)
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cartesian_products = {0:alphabet}
    for x in range(1,max_string_length,1):
        if x == 1:
            cartesian_products[x] = [[x,y] for x in alphabet for y in alphabet ]
        else:
            cartesian_products[x] = [[i for i in x] + [y] for x in cartesian_products[x-1] for y in alphabet ]
    sorted_list = []
    for x in cartesian_products[max_string_length-1]:
        for y in string_list:
            my_len = len(y)
            if "".join(x)[0:my_len] == y and y not in sorted_list:
                sorted_list.append(y)
    return sorted_list


def numeric_sort_easy(input_list):
    sorted_list = [0 for x in range(len(input_list))]
    for x in input_list:
        count = 0
        for y in input_list:
            if x>y:
                count += 1
        sorted_list[count] = x
    return sorted_list
	
def sort_min_to_max(int_list):
    # faster
    max = int_list[0]
    min = int_list[0]
    for x in int_list:
        if x < min:
            min = x
        elif x > max:
            max = x
    sorted_list = [y for x in [[i]*int_list.count(i) for i in range(min, max+1, 1) if i in int_list] for y in x]
    return sorted_list

def recursive_sort(l1):
    """
    length of input list l1 shoud not exceed maximum recursion depth -996
    """
    small = l1[0]
    if len(l1) == 1:
        return [small]
    index = l1.index(small)
    for x in l1:
        if x < small:
            small = x
            index = l1.index(x)
    del l1[index]
    return [small] + recursive_sort(l1

def tree_sort(l1):
    """
    recursive tree based sort, used sys.setrecusionlimit to override the default limit set by python which in 1000
    """
    sys.setrecursionlimit(10000)
    small = l1[0]
    if len(l1) == 1:
        return [small]
    if len(l1) <=3:
        index = l1.index(small)
        for x in l1:
            if x < small:
                small = x
                index = l1.index(x)
        del l1[index]
        return [small] + tree_sort(l1)
    left = []
    right = []
    for i,x in enumerate(l1):
        if x < small and i != 0:
            left.append(x)
        elif x > small and i != 0:
            right.append(x)
    if len(left) >=1 and len(right) >= 1:
        return tree_sort(left) + [small] + tree_sort(right)
    elif len(left) >=1:
        return tree_sort(left) + [small]
    elif len(right) >=1:
        return [small] + tree_sort(right)

	
def numeric_sort_single_list(int_list):
	# slower
    list_len = len(int_list)
    for i in [x for x in range(1,list_len, 1)]*list_len:
        current = int_list[i]
        previous = int_list[i-1]
        if current < previous:
            int_list[i] = previous
            int_list[i-1] = current
    return int_list	
	
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
	
def tcpSocket(localIp,localPort,remoteIp,remotePort,message):
    """
    Creates a tcp client socket and send some data
    To verify successfull TCP connection check for return code 0
    To verify TCP block check for return code 101
    """
    buffer_size = 1024
    list = message.split("|")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.bind((localIp, localPort))
        s.connect((remoteIp, remotePort))
        s.send(message)
        data = s.recv(buffer_size)
        print("Received message %s" % data)
        s.close()
        if ((data != message)&(list[1] != "ping")):
            return 1
        elif ((data != "0")&(list[1] == "ping")):
            return 512
    except socket.timeout:
        print("Socket connection got timed out")
        return 101
    except socket.error as socker:
        print("Socket error is%s" % socker)
        return 102
    return 0

def udpSocket(localIp,localPort,remoteIp,remotePort,message):
    """
    Creates a udp client socket and send some data
    To verify successfull UDP connection check for return code 0
    To verify UDP block check for return code 101
    """
    buffer_size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(10)
    try:
        s.bind((localIp, localPort))
        s.sendto(message, (remoteIp, remotePort))
        data = s.recv(buffer_size)
        print("Received message %s" % data)
        if data != message:
             return 1
    except socket.timeout:
        print("Socket connection got timed out")
        return 101
    except socket.error as socker: 
        print("Socket error is %s" % socker)
        return 102
    return 0
def pingout(remoteIp):
    """
    Do a ping to Remote IP.
    To verify successfull ping check for return code 0
    To verify ping block check for return code 101
    """
    try:
        cmd = "ping" + " -t 3 -o " + remoteIp + " > /dev/null 2>&1"
        data = os.system(cmd)
        print("execution status %s" % data)
        if data == 0:
            return 0
        else:
            return 512     
    except:
        print("not able to execute ping command")
        return 1

def pingin(localIp,agentIp,agentPort,messagetoagent):
    """
    Do a ping to local IP.
    To verify successfull ping check for return code 0
    To verify ping block check for return code 512
    """
    try:
        msg = messagetoagent + "|" + "NA" + "|" + "NA"
        data = tcpSocket(localIp,9997,agentIp,agentPort,messagetoagent)
        print("execution status %s" % data)
        if data == 0:
            return 0
        elif data == 512:
            return 512
    except:
        print("not able to execute ping command")
        return 1

def tcpSocketin(localIp,localPort,message,agentIp,agentPort,messagetoagent):
    """
    create a listening tcp server to wait for incoming tcp packet 
    and ask agent server to send a tcp message
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((localIp, localPort))
    server.settimeout(20)

    tcpSocket(localIp,9998,agentIp,agentPort,messagetoagent)
    
    try: 
        server.listen(1)
        conn, addr = server.accept()
        while 1:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
            print("recieved incoming message %s" % data)
            if data != message:
                return 1
        conn.close()
    except socket.timeout:
        print("Socket connection got timed out")
        return 101
    except socket.error as socker:
        print("Socket error at server is %s" % socker)
        return 102 
    server.close()
    return 0


def udpSocketin(localIp,localPort,message,agentIp,agentPort,messagetoagent):
    """
    create a listening udp server to wait for incoming udp message
    and ask agent server to send a udp message
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((localIp, localPort))
    server.settimeout(20)

    tcpSocket(localIp,9999,agentIp,agentPort,messagetoagent)

    try:
        while 1:
            data, addr = server.recvfrom(1024)
            if not data: break
            server.sendto(data, addr)
            print("recieved incoming message %s" % data)
            if data != message:
                return 1
            if data == message: break
    except socket.timeout:
        print("Socket connection got timed out")
        return 101
    except socket.error as socker:
        print("Socket error at server is %s" % socker)
        return 102
    server.close()
    return 0

def permutation_of_string(n):
    # fuction to generate a list of permutation of given string using permutations from itertools
    my_list = []
    perm_list = permutations(n)
    for perm in list(perm_list):
        my_list.append((''.join(perm)))
    return my_list

def list_cat(y):
    s1 = ""
    for x in y:
        s1 += x
    return s1


def custom_revo(a1):
    a = str(a1)
    c = [x for x in a ]
    b = len(a)

    for x in range(b//2):
        a1 = c[x]
        b1 = c[-(x+1)]
        c[x] = b1
        c[-(x+1)] = a1
    return c

def delete_using_rsync(dir_path):
    """
    delete dir with very huge size by using rsync 
    """
    try:
        cmd = "/tmp/emty_dir"""
        data = os.mkdir(cmd)
        cmd_2 = "rsync -a --delete " + cmd + " " + dir_path
        data = os.system(cmd_2)
        data = os.removedirs(dir_path)
        print("execution status %s" % data)
        if data == 0:
            return 0
        else:
            return 1
    except:
        print("not able to delete the dir")
        return 1

def triangle_area_based_on_coardinates(x, y):
    area1 = (x[0]*(y[1]-y[2])+x[1]*(y[2]-y[0])+x[2]*(y[0]-y[1]))/2
    return area1

def triangle_area(x, y):
    """
    triangle are without using formula, when both x, y cordinates are provided
    """
    for in1, xi in enumerate(x):
       for in2, yi in enumerate(y):
           if xi > 0 and yi > 0 and xi < yi and in1 == in2:
               base = xi
           elif xi > 0 and yi > 0 and yi < xi and in1 == in2:
               base = yi
           elif xi > 0 and yi > 0 and yi == xi and in1 == in2:
               base = xi
           elif xi == 0 and yi != 0 and in1 == in2:
               height = yi
           elif x != 0 and yi == 0 and in1 == in2:
               height = xi
    area1 = (base * height)/2
    return area1

def gcd_of_two_number(x,y):
    """
    GCD calculation without using Euler algorithm 
    """
    x_list = [i for i in range(1,x+1,1) if x%i == 0]
    y_list = [i for i in range(1,y+1,1) if y%i == 0]
    x_and_y = set(x_list) & set(y_list)
    return list(x_and_y)[-1]
	
def gcd_of_two_number_euler_method(x,y):
      """
    GCD or HCF calculation  using Euler algorithm 
    """
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x == y:
        return x
    elif x > y:
        return gcd_of_two_number_euler_method(x-y,y)
    return gcd_of_two_number_euler_method(x, y-x)




if __name__ == "__main__":
	A = [22, 40, 22, 22, 100, 0, 23,  99, 22, 1000, 1000,  700, 40, 2, 1, 11, 5, 9, 22]
	#A = []
	#A = [ i for i in range(30000)]
	#A[1] = 5
	S = numeric_sort_fast(A)
	print(S)

