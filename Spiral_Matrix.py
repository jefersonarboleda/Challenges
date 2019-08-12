#The aim is, when I introduce a 2D matrix (In a string form), I should return a array in clockwise spiral order.


def MatrixSpiral(strArr): 
    a=len(strArr)
    b=[]
    for i in range(a):
        k=ast.literal_eval(strArr[i])
        b.append(k)
    strArr=b
    z=[]
    i=0 #filas
    j=0#columnas
    m=len(strArr) #filas
    n=len(strArr[0]) #columna
    c=m*n
    while (i<=(m))&(j<=(n)):
        for l in range(i,n):
            z.append(strArr[i][l])
        i+=1
        if len(z)==c:
            break
    
        for l in range(i,m):
            z.append(strArr[l][n-1])
        for l in range(j,n-1):
            z.append(strArr[m-1][n-2-l])
        for l in range(i,m-1):
            z.append(strArr[m-1-l][j])
        n-=1
        m-=1
        j+=1
    s=[str(z) for z in z]
    s=",".join(s)
    return(s)
# keep this function call here  
print MatrixSpiral(raw_input())
