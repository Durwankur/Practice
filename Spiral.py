"""
A Sober Walk
Problem Statement
Our hoary culture had several great persons since time immemorial and king vikramaditya’s nava ratnas (nine gems) belongs to this ilk.They are named in the following shloka:


Among these, Varahamihira was an astrologer of eminence and his book Brihat Jataak is recokened as the ultimate authority in astrology.

He was once talking with Amarasimha,another gem among the nava ratnas and the author of Sanskrit thesaurus, Amarakosha.

Amarasimha wanted to know the final position of a person, who starts from the origin 0 0 and travels per following scheme.

Scheme
He first turns and travels 10 units of distance
His second turn is upward for 20 units
Third turn is to the left for 30 units
Fourth turn is the downward for 40 units
Fifth turn is to the right(again) for 50 units
… And thus he travels, every time increasing the travel distance by 10 units.

Test Cases
Case 1
Input : 3
Expected Output :-20 20
Case 2
Input: 4
Expected Output: -20 -20
Case 3
Input : 5
Expected Output : 30 -20
Case 4
Input : 7
Expected Output : 90 -20
"""

#Solution

n = int(input())
c = 'R'
dis = 10
x,y=0,0
for i in range(n):
    if c=='R':
        x=x+dis
        c='U'
        dis=dis+10
    elif c=='U':
        y=y+dis
        c='L'
        dis=dis+10
    elif c=='L':
        x=x-dis
        c='D'
        dis=dis+10
    elif c=='D':
        y=y-dis
        c='A'
        dis=dis+10
    elif c=='A':
        x=x+dis
        c='R'
        dis=dis+10
print(x,y)
