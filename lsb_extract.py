# moshe malka
path="pic.bmp"
f=open(path,'rb')
f.seek(0)   #go to the start of the file.
b=""
bytesArr=[]
while True:
    byte=f.read(1)  # read 1 byte at a time.
    bits = '{0:08b}'.format(ord(byte)) # get 8 bits.
    b+=str(bits[-1]) # get lsb from byte and concate them to new byte.
    if(len(b)==8):  # if we have 8 bits (1 byte) -> append it and restart variables.
        bytesArr.append(b)
        b=""
    if(len(bytesArr)==100): # if we reached 100 bytes - quit the proccess.
        break

out=[]
print "Outcome: "
for b1 in bytesArr:
    out.append(chr(int(b1,2)))
print ''.join(out)
f.seek(0)   #go to the start of the file.
