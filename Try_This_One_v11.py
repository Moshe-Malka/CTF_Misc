from subprocess import *
import socket
import time
import sys

def calc3(a,b,c):
    c=int(c)
    a=int(a)
    c3_o=0
    if(b=='-'):
        c3_o=a-c
    elif(b=='+'):
        c3_o=a+c
    elif(b=='/'):
        c3_o=a/c
    else:
        c3_o=a*c
    return c3_o

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False



hostname="35.158.25.165"
port=10237

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
q=s.recv(2048)
time.sleep(2)
content=s.recv(2048)
print "Content: "
print content

tamplate=content.split(" ")
tamplate[-1]= tamplate[-1].split("\n")[0]
print "Tamplate: "
print tamplate

def do_calc(tamplate):
    sc=['-','+','*','/']
    sc_out=[]
    nums_out=[]
    for a in tamplate:
        if a in sc:
            sc_out.append(a)
        else:
            nums_out.append(a)

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
                
    print "Out: "
    out_str = ' '.join(out)
    print out_str

    ans = 0
    index=0
    while (len(out)!= index):
        if(representsInt(out[index])):
            ans+=calc3(out[index],out[index+1],out[index+2])
            index+=3
        else:
            ans=calc3(ans,out[index],out[index+1])
            index+=2
            
    print "ANSWER: "+str(ans)
    return ans

ans=do_calc(tamplate)

ans=str(ans)+"\n"
toSend=ans.encode()
time.sleep(1)
print "Sending: "
print toSend
s.sendall(toSend)

while True:
    content=s.recv(2048)
    if(content=='Too Slow... Not a robot' or content=='You are not a robot'):
        print "Too Slow... Not a robot / You are not a robot"
        s.shutdown(socket.SHUT_WR)
        sys.exit(0)
    if(len(content)> 3):
        print content
        sys.exit(0)
