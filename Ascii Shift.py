x = input()
k = int(input())
print( "".join(chr(65+(ord(x)-65 -k )%26) for x in x))

#Shifting Characters by Specific Key Value(Cipher)
