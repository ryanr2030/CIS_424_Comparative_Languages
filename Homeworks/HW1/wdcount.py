#import system calls
import sys

#get the file name from the command line then put it on a buffer
fname=sys.argv[1]
file=open(fname,"r")

wdict={}    #Dictionary to store all of the words and their occurences
longwdict={} #Dictionary to store all of the words greater than 4 and occurences
maxword=""  #Variable to store the longest word

#store each unique word from the file in the wdict dictionary and count the occurences
for w in file.read().split():
    #convert each word to lowercase to prevent duplicate unique words from capitilization 
    w=w.lower()
    if w not in wdict:
        wdict[w]=1
        #keep track of which word is the longest in the file
        if len(w) > len(maxword):
            maxword=w
    else:
        wdict[w]+=1

#print the word count which is the sum of all of the values in the wdict dictionary
print("The word count is:",sum(wdict.values()))

#print the number of unique words which is the len of the wdict dictionary
print("The number of unique words is:", len(wdict))

#print the list of the unique words and their occurences in descending order
print("\nWords Contained in file '",fname,"'")
for k in sorted(wdict, key=wdict.get, reverse=True):
	print(k, wdict[k])
	if len(k) > 4:
            longwdict[k]=wdict[k]

#print the list of words greater than 4 characters in descending order
print("\nWords more than 4 characters in file '",fname,"'")
for k in sorted(longwdict, key=longwdict.get, reverse=True):
    print(k, longwdict[k])
print("")

#print the longest word
print("The longest word is '",maxword,"'")
