#RULES FOR THIS PARSER
#	<s>--><A>c|<B>c
#	<A>-->a<A>|a
#	<B>-->b<B>|b

#populates the list with words seperated by a space

import sys

#lexical analyzer function to iterate through the input
def lexan():
    global mitr
    try:
        return(next(mitr))
    except StopIteration:
        return('')

#match function is a utility function to check the token against your symbol table
def match(ch):
    global lookahead
    if ch==lookahead:
        #gets the next token in the input
        lookahead=lexan()
    else:
        print("Syntax Error")
        exit()
        
#WRITE THE S FUNCTION 
#   <s>--><A>c|<B>c
def S():
    global lookahead
    if lookahead=='a':
        A()
        match('c')
    elif lookahead=='b':
        B()
        match('c')
    else:
        print("Syntax Error")
        exit()
        
#WRITE THE A FUNCTION
#   <A>-->a<A>|a
def A():
    global lookahead
    match('a')
    if lookahead=='a':
        A()
    else:
        return
        
    
#WRITE THE B FUNCTION
#	<B>-->b<B>|b
def B():
    global lookahead
    match('b')
    if lookahead=='b':
        B()
    else:
        return


file=open(sys.argv[1],"r")
wlist=file.read().split()

#get the lexemes one by one
#mitr.next will get the next word
#convert the list into an interatable list mitr
mitr=iter(wlist)
#you typically want to look ahead to determine
lookahead=lexan()
S()
if lookahead=='':
    print("pass")
else:
    print("Syntax Error")


