n=int(input())
triangle=[]
for i in range(n):
    row=[1]*(i+1)
    for j in range(1,i):
        row[j]=triangle[i-1][j-1]+triangle[i-1][j]
    triangle.append(row)
print(triangle)

# OUTPUT:

# n=5
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

for i in range(n):
    print(" "*(n-i),end="")
    print(" ".join(map(str,triangle[i])))
    
# OUTPUT:

# n=5
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
