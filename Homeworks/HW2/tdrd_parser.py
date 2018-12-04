#       RULES FOR THIS PARSER
#	<s>--><X>z<Y>|<Y>z<X>
#	<X>-->x<X>|x
#	<Y>--y<Y>|y



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
#   <S>--><X>z<Y>|<Y>z<X>
#The S function uses the match and lookahead functions to check the syntax of the input by calling X() and Y() functions via Top down
#recursive descent
def S():
    global lookahead
    if lookahead=='x':
        X()
        match('z')
        Y()
    elif lookahead=='y':
        Y()
        match('z')
        X()
    else:
        print("Syntax Error")
        exit()
        
#WRITE THE X FUNCTION
#      RULE:
#   <X>-->x<X>|x
#this function checks for lone x characters and consecutive x characters
def X():
    global lookahead
    match('x')
    if lookahead=='x':
        X()
    else:
        return
        
    
#WRITE THE Y FUNCTION
#          RULE:
#	<Y>--y<Y>|y
#checks to for lone y characters and consecutive y characters
def Y():
    global lookahead
    match('y')
    if lookahead=='y':
        Y()
    else:
        return

#use the open function to create a buffer to the pointed file
file=open(sys.argv[1],"r")
#read the file from the buffer and store into wlist
wlist=file.read().split()

#get the lexemes one by one
#mitr.next will get the next word
#convert the list into an interatable list mitr
mitr=iter(wlist)

#Lookahead is used to always points to the token one index ahead of the current token
lookahead=lexan()

#Call the S() function to start top down recrusive descent 
S()

#print whether the string was valid or invalid 
if lookahead=='':
    print("pass")
else:
    print("Syntax Error")


