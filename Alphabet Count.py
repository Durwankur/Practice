#Solution 1:
s = 'hello'
t = {}
for i in s:
    if i in t:
        t[i]+=1
    else:
        t[i] = 1
print(t)


#Soultion 2:
string = 'durwankur'
s = { i : string.count(i) for i in string}
print (s)
