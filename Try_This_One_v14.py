from subprocess import *
import socket
import time
import sys
# hostname="35.158.25.165"
# port=10237

def connect(hostname,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    time.sleep(1)
    return s

def do_plus(arr):
    while('+' in arr):
        plus_index=arr.index('+')
        a = arr.pop(plus_index-1)   # left number
        b = arr.pop(plus_index)     # right number
        arr.pop(plus_index-1)       # operator (trash)
        c = str(int(a) + int(b))    # calculation
        arr.insert(plus_index-1,c)     # insertion

def do_minus(arr):
    while('-' in arr):
        minus_index=arr.index('-')
        a = arr.pop(minus_index-1)   # left number
        b = arr.pop(minus_index)     # right number
        arr.pop(minus_index-1)       # operator (trash)
        c = str(int(a) - int(b))    # calculation
        arr.insert(minus_index-1,c)     # insertion

def do_double(arr):
    while('*' in arr):
        double_index=arr.index('*')
        a = arr.pop(double_index-1)   # left number
        b = arr.pop(double_index)     # right number
        arr.pop(double_index-1)       # operator (trash)
        c = str(int(a) * int(b))    # calculation
        arr.insert(double_index-1,c)     # insertion

def do_divide(arr):
    while('/' in arr):
        divide_index=arr.index('/')
        a = arr.pop(divide_index-1)   # left number
        b = arr.pop(divide_index)     # right number
        arr.pop(divide_index-1)       # operator (trash)
        c = str(int(a) / int(b))    # calculation
        arr.insert(divide_index-1,c)     # insertion

def precedenceCalc(content):
    sc_out_t=[]
    sc_out=[]
    nums_out_t=[]
    nums_out=[]
    if( type(content) is not type([]) ): content = content.split(" ")
    for a in content:
        try:
            int(a)
            nums_out_t.append(a)
        except:
            sc_out_t.append(a)

    for num in nums_out_t:
        nums_out.append(num.replace("\n",""))
    for sc in sc_out_t:
        sc_out.append(sc.replace("\n",""))

    print "Special Charecters: "
    print sc_out
    print "Numbers: "
    print nums_out

    out=[]
    c_len= len(sc_out)+len(nums_out)
    b=True
    for x in range(c_len):
        if(b):
            out.append(nums_out.pop(0))
            b = not b
        else:
            if(len(sc_out)>0):
                out.append(sc_out.pop(0))
                b = not b

    print "Full Equation: "
    print out

    if('*' in out):
        do_double(out)
    if('/' in out):
        do_divide(out)
    if('+' in out):
        do_plus(out)
    if('-' in out):
        do_minus(out)
    return out[0]

def sendMsg(socket,msg):
    ans=str(msg)+"\n"
    toSend=ans.encode()
    print "Sending: "
    print toSend
    socket.sendall(toSend)
    time.sleep(1)

def do_main():
    c = connect("35.158.25.165",10237)
    time.sleep(1)
    while True:
        content=c.recv(2048)
        if('You are not a robot' in content):
            print content
            print "Trying Again"
            c = connect("35.158.25.165",10237)
            time.sleep(1)
            print '-'*80
            continue
        print "Content: "
        print content
        if('ALL THE ANSWERS' in content):
            content = content.split("ALL THE ANSWERS\n")[1]
            print "Filtered Content: "
            print content
        answer = precedenceCalc(content)
        sendMsg(c,answer)
        print '-'*80

if __name__=="__main__":
    do_main()
