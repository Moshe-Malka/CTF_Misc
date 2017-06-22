from subprocess import *
import socket
import time
import sys

sc=['-','+','*','/']

# hostname="35.158.25.165"
# port=10237

def connect(hostname,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    time.sleep(1)
    return s

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

def do_calc(template):
    sc_out=[]
    nums_out=[]
    splited = template.split(" ")
    for a in splited:
        if a in sc:
            sc_out.append(a)
        else:
            nums_out.append(a)
    for num in nums_out:
        num.replace("\n","")

    # print "Special Charecters: "
    # print sc_out
    # print "Numbers: "
    # print nums_out

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

    # print "Out: "
    # out_str = ' '.join(out)
    # print out_str

    ans = 0
    index=0
    while (len(out)!= index):
        if(representsInt(out[index])):
            ans+=calc3(out[index],out[index+1],out[index+2])
            index+=3
        else:
            ans=calc3(ans,out[index],out[index+1])
            index+=2

    #print "ANSWER: "+str(ans)
    return ans

def precedenceCalc(content):
    sc_out=[]
    nums_out_t=[]
    nums_out=[]
    if( type(content) is not type([]) ): content = content.split(" ")
    for a in content:
        if a in sc:
            sc_out.append(a)
        else:
            nums_out_t.append(a)
    for num in nums_out_t:
        nums_out.append(num.replace("\n",""))

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
    out_str = ' '.join(out)
    print out_str

    if('*' in out):
        # get all indexes of '*' operator
        star_indexs=[]
        for s in out:
            if(s=='*'):
                star_indexs.append(out.index(s))
        # iterate by the amount of the operator found and calculate multiplication
        for i in range(len(star_indexs)):
            star_index = star_indexs[i]
            a = out.pop(star_index-1)
            b = out.pop(star_index)
            out.pop(star_index-1)
            c = int(int(a) * int(b))
            out.insert(star_index-1,str(c))

    if('/' in out):
        # get all indexes of '/' operator
        divide_indexs=[]
        for s in out:
            if(s=='/'):
                divide_indexs.append(out.index(s))
        # iterate by the amount of the operator found and calculate multiplication
        for i in range(len(divide_indexs)):
            divide_index = divide_indexs[i]
            a = out.pop(divide_index-1)
            b = out.pop(divide_index)
            out.pop(divide_index-1)
            c = int(int(a) / int(b))
            out.insert(divide_index-1,str(c))

    # here we are calculating every operator other then '*' and '/'
    pass_str = " ".join(out)
    ans = do_calc(pass_str)
    return ans  # returns calculated list

#print precedenceCalc("-6 5 12 34 / * +")
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
            print "Failed ! Trying Again"
            c = connect("35.158.25.165",10237)
            time.sleep(1)
            continue
        print "Content: "
        print content
        if('ALL THE ANSWERS' in content):
            content = content.split("ALL THE ANSWERS\n")[1]
            print "Filtered Content: "
            print content
        ans = precedenceCalc(content)
        print ans
        sendMsg(c,ans)
        print '-'*80

if __name__=="__main__":
    do_main()
