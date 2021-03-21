#Solution 1
def rot(arr, d):
    return arr[d:]+arr[:d]
        
n,d = map(int,input().split(' '))
a = list(map(int, input().split(' ')))

result = rot(a, d)
print(*result)

#Solution 2
def rotLeft(a, d):
    new = []
    for i in range(len(a),0,-1):
        new.append(a[d-i])
    return new
  
#Soultion 3
def rot(a, d):
    for i in range(d):
        for j in range(0,len(a)-1):
            a[i]= (i + (len(a)-d))%n
    return a
