#Have the function SimplePassword(str) take the str parameter being passed and determine if it passes as a valid password 
#that follows the list of constraints:

#1. It must have a capital letter.
#2. It must contain at least one number.
#3. It must contain a punctuation mark.
#4. It cannot have the word "password" in the string.
#5. It must be longer than 7 characters and shorter than 31 characters.

#If all the above constraints are met within the string, the your program should return the string true, 
#otherwise your program should return the string false. For example: if str is "apple!M7" then your program 
#should return "true".

import string 

def pun(a):
    j=[]
    for i in a:
        if i in string.punctuation:
            j.append(i)
    return(len(j))

def SimplePassword(str): 
    b='password'
    c=[i.isupper() for i in str]  # Capital letter
    n=c.count(True)
    d=[i.isdigit() for i in str] # Number
    m=d.count(True)
    p=pun(str)
    j=str.find(b)
    l=len(str)
    if ((n>=1)&(m>=1)&(p==1)&(j==-1)&(7<l<31)):
        a='true'
    else:
        a='false'
    # code goes here 
    return a
    
# keep this function call here  
print SimplePassword(raw_input())
