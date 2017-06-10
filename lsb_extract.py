import binascii
import os
import io
from PIL import Image

path="pic.bmp"
f=open(path,'rb')
f.seek(0)
b=""
bytesArr=[]
while True:
    byte=f.read(1)
    #print binascii.hexlify(byte)
    #print byte
    bits = '{0:08b}'.format(ord(byte))
    #print bits
    lsb=[]
    b+=str(bits[-1])
    if(len(b)==8):
        #print "new Byte: "+ str(b)
        bytesArr.append(b)
        b=""
        #break
    if(len(bytesArr)==1000):
        break

#print ''.join(bytesArr)

out=[]
o=""
print "Outcome: "
for b1 in bytesArr:
    h=hex(int(b1,2))
    print chr(int(b1,2))
    for a in range(7):    
        o+=h
    out.append(o)
    o=""
print out


f.seek(0)
