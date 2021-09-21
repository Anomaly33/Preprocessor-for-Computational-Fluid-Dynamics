# Please add the *.txt file to your desired location before proceeding.
from matplotlib import pyplot as plt
import numpy as np
import math

j = 0
k = 0
m = 0
file = ''
a = []
try:
    n = input('Enter the name of your file: ')
    direc=input('''Enter the file path or directory to the file :
For example:C:/Users/user/Desktop''')
    f = open(f'{direc}/{n}.txt', 'r')  # Opening the user entered file in read mode.
    print('File successfully added!')

except FileNotFoundError:
    print('File not found! Please check the name of the file and its existence on path provided and try again.')
    exit()
files = f.readlines()
for line in files:
    file += line.strip()  # Storing the contents of files in file(a string).
    file += '\n'
    j += 1
a = file.split('\n')  # Converting the string file to a list.
l = len(a)
res = [int(i) for i in a if i.isdigit()]  # Extracting the number of nodes and triangular control volumes from a.
b, c = res
print(f'Number of nodes = {b}')
print(f'Number of triangles = {c}')
for i in range(l - 1):
    if a[i] == str(b):
        a.remove(str(b))  # Trimming the list a.
for i in range(l - 2):
    if a[i] == str(c):
        a.remove(str(c))  # Trimming the list a.

a.pop(-1)

d = [None] * (c * 3 + b * 2)
cd = [None] * (b * 2)
tri = [None] * (c * 3)
x = [None] * b
y = [None] * b
for i in range(b):
    d[k], d[k + 1] = a[i].split(' ')  # Storing the information of coordinates of nodes in a list d.
    k += 2

k = b * 2
m = b * 2
i = b

while k <= c * 3 + b * 2 - 1:
    d[k], d[k + 1], d[k + 2] = a[i].split(' ')  # Storing the information of the triangular control volumes in a list d.
    k += 3
    i += 1

for i in range(b * 2):
    cd[i] = d[i]
m = 0
for n in range(b * 2, c * 3 + b * 2, 1):
    tri[m] = d[n]
    m += 1
q = 0
w = 0
for i in range(len(cd)):
    if i % 2 == 0:
        x[q] = cd[i]
        x[q] = float(x[q])
        q += 1
    else:
        y[w] = cd[i]
        y[w] = float(y[w])
        w += 1

# Plotting the nodes.
plt.scatter(x, y)
s = np.arange(1, b + 1, 1)
for i, txt in enumerate(s):
    plt.annotate(txt, (x[i], y[i]))  # Number the grid points as per the convention

for i in range(len(cd)):
    cd[i] = float(cd[i])
for i in range(len(tri)):
    tri[i] = int(tri[i])

# Plotting the triangular sub-domain.
i = 0
while i < len(tri):

    plt.plot([x[tri[i] - 1], x[tri[i + 1] - 1]], [y[tri[i] - 1], y[tri[i + 1] - 1]], 'b')
    plt.plot([x[tri[i + 1] - 1], x[tri[i + 2] - 1]], [y[tri[i + 1] - 1], y[tri[i + 2] - 1]], 'b')
    plt.plot([x[tri[i + 2] - 1], x[tri[i] - 1]], [y[tri[i + 2] - 1], y[tri[i] - 1]], 'b')
    i += 3
h = i
plt.title('Triangular Control Volumes')

i = 0
g = 0
while i < len(x):
    if x[i] <= max(x) and y[i] == min(y):
        g += 1
    elif x[i] == min(x) and y[i] <= max(y):
        g += 1
    elif x[i] <= max(x) and y[i] == max(y):
        g += 1
    elif x[i] == max(x) and y[i] <= max(y):
        g += 1
    i += 1
print(f'The number of boundary edges = {g}')
print(f'Number of edges = {int((h - g) / 2)}')

i = 0
j = 0
s1 = 0
s2 = 0
s3 = 0
area = 0
sp = 0
# Finding area of the Triangular sub domains using Heron's Formula.
while i < len(tri):
    s1 = math.sqrt((x[tri[i] - 1] - x[tri[i + 1] - 1]) ** 2 + (y[tri[i] - 1] - y[tri[i + 1] - 1]) ** 2)
    s2 = math.sqrt((x[tri[i + 1] - 1] - x[tri[i + 2] - 1]) ** 2 + (y[tri[i + 1] - 1] - y[tri[i + 2] - 1]) ** 2)
    s3 = math.sqrt((x[tri[i + 2] - 1] - x[tri[i] - 1]) ** 2 + (y[tri[i + 2] - 1] - y[tri[i] - 1]) ** 2)
    sp = (s1 + s2 + s3) / 2
    area = math.sqrt(sp * (sp - s1) * (sp - s2) * (sp - s3))
    print(f'Area of Triangle {j + 1} = {area} sq. units')
    s1 = 0
    s2 = 0
    s3 = 0
    area = 0
    sp = 0
    i += 3
    j += 1

ctdx = [None] * c
ctdy = [None] * c
i = 0
j = 0
while i < len(tri):
    ctdx[j] = ((x[tri[i] - 1]) + (x[tri[i + 1] - 1]) + (x[tri[i + 2] - 1])) / 3
    ctdy[j] = ((y[tri[i] - 1]) + (y[tri[i + 1] - 1]) + (y[tri[i + 2] - 1])) / 3
    i += 3
    j += 1
# Plotting the centroids of the traingular sub-domains.
plt.scatter(ctdx, ctdy)
w = np.arange(1, c + 1, 1)
for i, txt in enumerate(w):
    plt.annotate(txt, (ctdx[i], ctdy[i]))  # Number the centroids as per the convention

# The neighbors of each edge.
ce = []
i = 0
j = 0
v1, v2, v3 = 0, 0, 0
while i < len(tri):
    v1 = tri[i]
    v2 = tri[i + 1]
    v3 = tri[i + 2]
    j = 0
    while j < len(tri):
        if j != i:
            k = 0
            if v1 == tri[j] or v1 == tri[j + 1] or v1 == tri[j + 2]:
                k += 1
            if v2 == tri[j] or v2 == tri[j + 1] or v2 == tri[j + 2]:
                k += 1
            if v3 == tri[j] or v3 == tri[j + 1] or v3 == tri[j + 2]:
                k += 1
            if k == 2:
                if v1 == tri[j] or v1 == tri[j + 1] or v1 == tri[j + 2]:
                    k = 1
                else:
                    k = 0
                if k == 1:
                    ce.append(v1)
                if v2 == tri[j] or v2 == tri[j + 1] or v2 == tri[j + 2]:
                    k = 1
                else:
                    k = 0
                if k == 1:
                    ce.append(v2)
                if v3 == tri[j] or v3 == tri[j + 1] or v3 == tri[j + 2]:
                    k = 1
                else:
                    k = 0
                if k == 1:
                    ce.append(v3)
        j += 3

    v1, v2, v3 = 0, 0, 0
    i += 3
# To maintain the convention of numbering the edges.
i = 0
while i < len(ce):
    if ce[i] > ce[i + 1]:
        ce[i], ce[i + 1] = ce[i + 1], ce[i]
    i += 2

ce1 = []
i = 0
while i < len(ce):
    ce1.append([ce[i], ce[i + 1]])
    i += 2
ce2 = []
[ce2.append(x) for x in ce1 if x not in ce2]
ce21 = ce2.copy()

i = 0
while i < len(ce2):
    if ce2[i][0] - ce2[i][1] == 1 or ce2[i][0] - ce2[i][1] == -1:
        ce2.remove(ce2[i])
    i += 1

k = 0
v = 0
i = 0
j = 0
t = []
while i < len(ce2):
    j = 0
    v = 0
    while j < len(tri):
        v += 1
        if tri[j] == ce2[i][0] or tri[j] == ce2[i][1]:
            k += 1
        if tri[j + 1] == ce2[i][0] or tri[j + 1] == ce2[i][1]:
            k += 1
        if tri[j + 2] == ce2[i][0] or tri[j + 2] == ce2[i][1]:
            k += 1
        if k == 2:
            t.append(v)
        k = 0
        j += 3
    i += 1

i = 0
j = 0
while i < len(t):
    print(
        f'The left neighbor of edge {ce2[j][0]}-{ce2[j][1]} is triangle {t[i]} and the right neighbour is {t[i + 1]}.')
    i += 2
    j += 1

# Finding the boundary edges.
t1 = []
i = 0
while i < len(tri):
    t1.append(tri[i])
    t1.append(tri[i + 1])
    t1.append(tri[i + 1])
    t1.append(tri[i + 2])
    t1.append(tri[i + 2])
    t1.append(tri[i])
    i += 3
# To maintain the convention of numbering the boundary edges.
i = 0
while i < len(t1):
    if t1[i] > t1[i + 1]:
        t1[i], t1[i + 1] = t1[i + 1], t1[i]
    i += 2

t2 = []
i = 0
while i < len(t1):
    t2.append([t1[i], t1[i + 1]])
    i += 2
t3 = []
[t3.append(x) for x in t2 if x not in t3]
t4 = [x for x in t3 if x not in ce21]
i = 0
j = 0
print('The boundary edges are : ')
while i < len(t4):
    print(f'{j + 1}) {t4[i][0]}-{t4[i][1]}')
    i += 1
    j += 1

# Finding the boundary nodes and their coordinates.
i = 0
j = 0
bex = [None] * g
bey = [None] * g
while i < len(x):
    if x[i] <= max(x) and y[i] == min(y):
        bex[j] = x[i]
        bey[j] = y[i]
        j += 1
    elif x[i] == min(x) and y[i] <= max(y):
        bex[j] = x[i]
        bey[j] = y[i]
        j += 1
    elif x[i] <= max(x) and y[i] == max(y):
        bex[j] = x[i]
        bey[j] = y[i]
        j += 1
    elif x[i] == max(x) and y[i] <= max(y):
        bex[j] = x[i]
        bey[j] = y[i]
        j += 1
    i += 1

bnn = [None] * g
j = 0
i = 0
while i < len(x) and j < len(bex):
    if x[i] == bex[j] and y[i] == bey[j]:
        bnn[j] = i + 1
        i += 1
        j += 1
    else:
        i += 1

print('The boundary nodes and their coordinates are :')
for i in range(0, len(bex), 1):
    print(f'Node {bnn[i]} : ({bex[i]},{bey[i]})')

# Triangles sharing a common node.
i = 0
j = 0
v = 0
t5 = []
while i < len(s):
    v = 0
    j = 0
    while j < len(tri):
        v += 1
        if tri[j] == s[i] or tri[j + 1] == s[i] or tri[j + 2] == s[i]:
            t5.append(v)
        j += 3
    print(f'The Triangles sharing the node {s[i]} are : ')
    print(*t5, sep=", ")
    t5 = []
    i += 1

# Neighboring triangles of each triangular sub-domain.
t6 = []
i = 0
j = 0
v1, v2, v3 = 0, 0, 0
while i < len(tri):
    v1 = tri[i]
    v2 = tri[i + 1]
    v3 = tri[i + 2]
    j = 0
    v = 0
    while j < len(tri):
        v += 1
        if j != i:
            k = 0
            if v1 == tri[j] or v1 == tri[j + 1] or v1 == tri[j + 2]:
                k += 1
            if v2 == tri[j] or v2 == tri[j + 1] or v2 == tri[j + 2]:
                k += 1
            if v3 == tri[j] or v3 == tri[j + 1] or v3 == tri[j + 2]:
                k += 1
            if k == 2:
                t6.append(v)
        j += 3
    t7 = []
    [t7.append(x) for x in t6 if x not in t7]
    print(f'The neighbouring triangles of triangle {int(i / 3 + 1)} are :')
    print(*t7, sep=", ")
    t6 = []
    v1, v2, v3 = 0, 0, 0
    i += 3

# Neighbors of each node.
i = 0
j = 0
t8 = []
while i < len(s):

    j = 0
    while j < len(tri):

        if tri[j] == s[i] or tri[j + 1] == s[i] or tri[j + 2] == s[i]:
            t8.append(tri[j])
            t8.append(tri[j+1])
            t8.append(tri[j + 2])
            t8.remove(s[i])
        j += 3
    t9 = []
    [t9.append(x) for x in t8 if x not in t9]
    print(f'The neighbors of the node {s[i]} are : ')
    print(*t9, sep=", ")
    t8 = []
    i += 1

# Angles made by the edges of the triangular sub-domains to the horizontal-axis.
ce21.extend(t4)
n1,n2,n1x,n1y,n2x,n2y,angleInDegrees=0,0,0,0,0,0,0
i=0
while i<len(ce21):
    n1=ce21[i][0]
    n2=ce21[i][1]
    n1x=x[ce21[i][0]-1]
    n1y=y[ce21[i][0]-1]
    n2x = x[ce21[i][1]-1]
    n2y = y[ce21[i][1]-1]
    deltaX= n2x-n1x
    deltaY=n2y-n1y
    if deltaX==0.0:
        angleInDegrees=90.0
    elif deltaY==0.0:
        angleInDegrees=0.0
    else:
        angleInDegrees = np.arctan(deltaY / deltaX) * 180 / np.pi
    if angleInDegrees<0.0:
        angleInDegrees+=360.0
    print(f'The angle made by the edge {ce21[i][0]}-{ce21[i][1]} to the horizontal axis is {angleInDegrees}°')
    i += 1
    n1, n2, n1x, n1y, n2x, n2y, angleInDegrees = 0, 0, 0, 0, 0,0,0

# Showing the grid.
plt.show()

#END#
