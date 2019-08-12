#Have the function WordSplit(strArr) read the array of strings stored in strArr, which will contain 2 elements: 
#the first element will be a sequence of characters, and the second element will be a long string of comma-separated words,
#in alphabetical order, that represents a dictionary of some arbitrary length. For example: strArr can be: 
#["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]. Your goal is to determine if the first element in
#the input can be split into two words, where both words exist in the dictionary that is provided in the second input. 
#In this example, the first element can be split into two words: hello and cat because both of those words are in the dictionary.
#Your program should return the two words that exist in the dictionary separated by a comma. So for the example above, 
#your program should return hello,cat. There will only be one correct way to split the first element of characters 
#into two words. If there is no way to split string into two words that exist in the dictionary, return the string not possible.
#The first element itself will never exist in the dictionary as a real wor


def WordSplit(strArr): 
    b=strArr[0]
    c=strArr[1].split(',')
    p=[]
    p1=[]
    for i in range(len(c)):
        r=b.split(c[i])
        if len(r)==2:
            k=r[0]+r[1]        
            p.append(k)
    for j in range(len(p)):
        if c.count(p[j])!=0:
            p1.append(p[j])
    l=[]
    if p1==[]:
        l='not possible'
    else:
        for i in range(len(p1)):
            for j in range(len(p1)):
                n=p1[i]+p1[j]
                if n==b:
                    l.append(p1[i])
                    l.append(p1[j])
                    l=','.join(l)
            
    # code goes here 
    return l
    
# keep this function call here  
print WordSplit(raw_input())
