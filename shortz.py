
def _shortz(num):
    if(num==1 or num==0):
        return num
    if(num%2==0):
        return (num//4)
    if(num%2==1):
        return ((3*num)+1)


def Shortz(n):
    counter=0
    while True:
        counter+=1
        n=_shortz(n)
        if(n==0 or n==1):
            break
    return int(counter)

def ShortzSum(num):
    sum1=0
    out=[]
    out.append(num)
    while True:
        num=_shortz(num)
        out.append(num)
        if(num==1 or num==0):
            break
    #print out
    for o in out:
        sum1+=o
    return int(sum1)
