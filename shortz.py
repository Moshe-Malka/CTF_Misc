
def Shortz(num):
    if(num>0):print num
    if(num==1 or num==0):
        print "END"
    elif(num%2==0):
        n1=(num//4)
        Shortz(n1)
    else:
        n2=((3*num)+1)
        Shortz(n2) 
# <Not Finished>
def ShortzSum(num):
    m_sum=num
    if(num%2==0):
        n1=(num//4)
        m_sum+=n1
        ShortzSum(n1)
    elif(num==1):
        m_sum+=1
        print m_sum
    else:
        n2=((3*num)+1)
        m_sum+=n2
        ShortzSum(n2)
