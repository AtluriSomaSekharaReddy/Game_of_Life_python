input_=[0,1,0, 0,0,1, 1,1,1, 0,0,0]
l=[]
x=0
for i in range(3,len(input_)+1,3):
    l.append(input_[x:i])
    x+=3
# print(input_)
print(l)
l_rows=len(l)
l_coul=len(l[0])
def countNeighbors (rows,coul):
    temp=0
    for i in range(rows-1,rows+2):
        for j in range(coul-1,coul+2):
            if((i==rows and j==coul) or i<0 or j<0 or i==l_rows or j==l_coul):
                continue
            if l[i][j] in [1,3]:
                temp+=1
    return temp
for i in range(l_rows):
    for j in range(l_coul):
        temp = countNeighbors(i,j)
        if l[i][j]:
            if temp in [2,3]:
                l[i][j]=3
        elif temp==3:
            l[i][j]=2
for i in range(l_rows):
    for j in range(l_coul):
        if l[i][j]==1:
            l[i][j]=0
        elif l[i][j] in [2,3]:
            l[i][j]=1
print(l)