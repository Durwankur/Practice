v = 'aeiou'
s = input()
count = 0
for i in v:
    for j in range(len(s)):
        if s[j] == i:
            count += 1
print (count)
