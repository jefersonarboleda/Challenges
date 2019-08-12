#Have the function WildcardCharacters(str) read str which will contain two strings separated by a space. 
#The first string will consist of the following sets of characters: +, *, and {N} which is optional. 
#The plus (+) character represents a single alphabetic character, the asterisk (*) represents a sequence of the same character
#of length 3 unless it is followed by {N} which represents how many characters should appear in the sequence where N 
#will be at least 1. Your goal is to determine if the second string exactly matches the pattern of the first string in the 
#input.

#For example: if str is "++*{5} gheeeee" then the second string in this case does match the pattern, so your program should
#return the string true. If the second string does not match the pattern your program should return the string false.


def hay_num(c):
    for i in range(len(c)):
        if (c[i]!='+')and(c[i]!='*'):
            ind=c.index(c[i])
            num=int(c[i])
            break
            
        else:
            ind=False
            num=0
    return(ind,num)

def hay_plus(z1):
    j=[]
    for i in range(len(z1)):
        if z1[i]=='+':
            j.append(i)
            continue
        
    return(j)

def WildcardCharacters(str): 
    b=str.split(' ')
    c=[i for i in b[0]]
    if c.count('{')==1:
        c.remove('{')
    if c.count('}')==1:
        c.remove('}')
    k,l=hay_num(c)
    if k==False:
        suma=c.count('+')+c.count('*')*3
        asw=(suma==len(b[1]))
    else:
        if k==(len(b[0])-1):
            suma=c.count('+')+c.count('*')*l
            asw=(suma==len(b[1]))
        else:
            z1=c[:k]
            z2=c[k+1:]
            g=hay_plus(z1)
            if g==[ ]:
                suma=z1.count('+')+z1.count('*')*l+z2.count('+')+z2.count('*')*3
                asw=(suma==len(b[1]))
            else:
                suma=z1[:g[0]].count('*')*3+z1[:g[0]].count('+')+z1[g[0]:].count('+')+z1[g[0]:].count('*')*l
                asw=(suma==len(b[1]))

    # code goes here 
    return(asw) 
    
# keep this function call here  
print WildcardCharacters(raw_input())
