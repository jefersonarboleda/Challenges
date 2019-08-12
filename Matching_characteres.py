#Have the function MatchingCharacters(str) take the str parameter being passed and determine the largest number of unique
#characters that exists between a pair of matching letters anywhere in the string. For example: if str is "ahyjakh" then there
#are only two pairs of matching letters, the two a's and the two h's. Between the pair of a's there are 3 unique characters:
#h, y, and j. Between the h's there are 4 unique characters: y, j, a, and k. So for this example your program should return 4.

#Another example: if str is "ghececgkaem" then your program should return 5 because the most unique characters exists within
#the farthest pair of e characters. The input string may not contain any character pairs, and in that case your program should
#just return 0. The input will only consist of lowercase alphabetic characters.


def MatchingCharacters(str): 
    b=[i for i in str]
    count=[]
    for i in range(0,len(b)):
        for j in range(1,len(b)):
            if (b[i]==b[-j]):
                z=b[i+1:-j]
                z1=b[i+1:-j]
                if (len(z)!=0):
                    count.append(len(list(set(z1))))
                    
                    
            else:
                count.append(0)
                continue
    return max(count)
    
# keep this function call here  
print MatchingCharacters(raw_input())
