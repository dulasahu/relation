import os
import socket
from itertools import permutations

def numeric_sort_easy(input_list):
    sorted_list = [0 for x in range(len(input_list))]
    for x in input_list:
        count = 0
        for y in input_list:
            if x>y:
                count += 1
        sorted_list[count] = x
    return sorted_list
	
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





if __name__ == "__main__":
	A = [22, 40, 22, 22, 100, 0, 23,  99, 22, 1000, 1000,  700, 40, 2, 1, 11, 5, 9, 22]
	#A = []
	#A = [ i for i in range(30000)]
	#A[1] = 5
	S = numeric_sort_fast(A)
	print(S)

