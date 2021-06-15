
r,k = map(int,input().split(' '))
count = 0
for i in range(1,r+1):
    binary = bin(i).lstrip('0b')
    occ = 0
    while True:
        try:
            indx = binary.index('101')
            occ += 1
            binary = binary[indx+2:]
        except: 
            break
    if occ>=k:
        count +=1
print (count)
    
