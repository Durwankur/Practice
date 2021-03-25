gro = ['bread', 'milk', 'butter']
print (list(enumerate(gro)))

for i,item in enumerate(gro, 101):
    print(i,item)
    
    '''
Output:

[(0, 'bread'), (1, 'milk'), (2, 'butter')]
101 bread
102 milk
103 butter
'''
