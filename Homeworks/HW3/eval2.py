#!/usr/bin/python
import sys
from math import*
#       RULES FOR THIS PARSER
#	<prog>      ::= <decl-list><stmt-list>
#       <decl-list>  ::= <decl> {<decl>}
#	<decl>      ::=<type> <id_list> ;
#	<type>      ::= int | real
#       <id_list>   ::= id {, id}
#       <stmt-list> ::= <stmt>{<stmt>}
#       <stmt>      ::= id = <expr> ; |
#                       id = <expr> if <cond> else <expr> ; |
#                       printi <expr> ; |
#                       printr <expr> ; |
#       <expr>      ::= <term>{ + <term> | - <term> }
#       <term>      ::= <factor> { * <factor> | / <factor> }
#       <factor>    ::= <base> ^ <factor> | <base>
#       <base>      ::= (<expr>) | id | intnum | realnumber
#       <cond>      ::= <oprnd> < <oprnd> |
#                       <oprnd> <= <oprnd> |
#                       <oprnd> > <oprnd> |
#                       <oprnd> >= <oprnd> |
#                       <oprnd> == <oprnd> |
#                       <oprnd> != <oprnd> 
#       <oprnd>     ::= id | intnum |realnumber


#dictionary to store the value and id of a variable
valList = {}
#dictionary to store the id and the variable type of a variable
typeList = {}
#dictionary to store execution strings
execute= {}

#lexical analyzer function to iterate through the input
def lexan():
    global mitr
    try:
        return(next(mitr))
    except StopIteration:
        return('')

#match function is a utility function to check the token against your symbol table
#Removed to iteration in this to do manually
def match(ch):
    global lookahead
    if ch==str(lookahead):
        return True
    return False

#function to return the variable type
def ty(num):
    if num.isdigit() is True:
        return 'int'
    try:
        float(num)
        return 'real'
    except ValueError:
        return type(num)


def exeC():
    global printcount
    i=0
    while i < printcount:
        print(execute[i])
        i+=1





#WRITE THE PROG FUNCTION
#	<prog>      ::= <decl-list><stmt-list>
def prog():
    global current
    global lookahead


    if match('') is False:
        current=lookahead
        if current == 'real' or current == 'int':
            dec_list()
        else:
            stmt_list()
        prog()
    else:
        exeC()
        return





#WRITE THE DEC-LIST FUNCTION
#     <dec-list>  ::= <decl> {<decl>}
# This function stores the declared variable and their value
def dec_list():
    global lookahead
    global current
    lookahead=lexan()
    if current==';':
        return
    decl()
    dec_list()



#WRITE THE DECL FUNCTION
#	<decl>      ::=<type> <id_list> ;
# the decl function declares the
def decl():
    global lookahead
    global current
    if match(';') is True:
            current = lookahead
            return
    elif match(',') is True:
            lookahead=lexan()
            type_()
            decl()
    else:
        type_()
        decl()

#WRITE THE TYPE FUNCTION
#	<type>      ::= int | real
# the type function stores the type and value of the token in
# the valList and typeList dictionaries
def type_():
    global lookahead
    if current=='int' and lookahead not in valList:
        typeList[lookahead] = current
        valList[lookahead]=0
        lookahead=lexan()

    elif current=='real' and lookahead not in valList:
        typeList[lookahead] = current
        valList[lookahead]=0
        lookahead=lexan()

    else:
        print("Syntax Errors")
        exit()
        
    
#WRITE THE STATEMENT LIST FUNCTION
#       <stmt-list> ::= <stmt>{<stmt>}
# The statement list function determines if it is a valid statement within the language
def stmt_list():
    global lookahead
    global current
    if current in valList.keys() or current=='printi' or current=='printr':
        stmt()
        stmt_list()
    elif current==';':
        lookahead=lexan()
        return
    else:
        print('Syntax Errors')
        exit()


#WRITE THE STATEMENT FUNCTION
#       <stmt>      ::= id = <expr> ; |
#                       id = <expr> if <cond> else <expr> ; |
#                       printi <expr> ; |
#                       printr <expr> ; |
#determines if the statement is a valid statement in the language according to the above rule
def stmt():
    global lookahead
    global current
    global result
    global printcount
    result=0

    if match(';') is True:
        current=lookahead
        return
    elif current=='printi':
        lookahead=lexan()
        expr()
        if isinstance(result,int) is False:
            print("Syntax Errors.")
            exit()
        execute[printcount]=result
        printcount+=1
        stmt()

    elif current=='printr':
        lookahead=lexan()
        expr()
        execute[printcount]=result
        printcount+=1
        stmt()
    else:
        lookahead=lexan()
        if match('=') is True:
            lookahead=lexan()
            expr()
            if typeList[current]=='real':
                valList[current] = float(result)
            elif typeList[current]=='int':
                if isinstance(result,int) is False:
                    print("Syntax Errors.")
                    exit()
                valList[current] = int(result)

            if match('if'):
                lookahead=lexan()
                temp=cond()
                if temp is True:
                    while match(';') is False:
                        lookahead=lexan()
                    return
                elif temp is False:
                    lookahead=lexan()
                    if match('else'):
                        lookahead=lexan()
                        expr()
                        if typeList[current] == 'real':
                            valList[current] = float(result)
                        elif typeList[current] == 'int':
                            if isinstance(result,int) is False:
                                print("Syntax Errors.")
                                exit()
                            valList[current] = int(result)
                            stmt()
                    else:
                        print('Syntax Errors')
                        exit()



            elif match(';'):
                current=lookahead
                return
            else:
                print('Syntax Errors')
                exit()


#WRITE THE EXPR FUNCTION USE THE BELOW RULE
#       <expr>      ::= <term>{ + <term> | - <term> }
#Determines if the expression is a valid expression within the language 
def expr():
    global lookahead
    global current
    global exp
    global result
    term()
    if lookahead==';':
        if '++' in exp or '--' in exp or '+-' in exp or '-+' in exp:
            print('Syntax Errors')
            exit()

        else:
            try:
                result=eval(exp)
            except SyntaxError:
                print('Syntax Errors')
                exit()
            exp=''
            return
    elif lookahead=='if':
        try:
            result=eval(exp)
        except SyntaxError:
            print('Syntax Errors')
            exit()

        exp=''
        return
    elif match('+'):
        exp+='+'
        lookahead=lexan()
        expr()
    elif match('-'):
        exp+='-'
        lookahead=lexan()
        expr()
    else:
        print('Syntax errors')
        exit()

#WRITE THE TERM FUNCTION ACCORDING TO THE RULE BELOW
#       <term>      ::= <factor> { * <factor> | / <factor> }
def term():
    global lookahead
    global current
    global exp
    global result
    factor()
    if match('*'):
        exp+='*'
        lookahead=lexan()
        term()
    elif match('/'):
        exp+='/'
        lookahead=lexan()
        term()
    else:
        return
    
#WRITE THE FACTOR FUNCTION
#       <factor>    ::= <base> ^ <factor> | <base>
def factor():
    global lookahead
    global current
    global exp
    base()
    if match('^'):
        exp+='**'
        lookahead=lexan()
        factor()
    else:
        return


#WRITE THE BASE FUNCTION
#       <base>      ::= (<expr>) | id | intnum | realnumber
def base():
    global lookahead
    global exp

    if match('('):
        exp+='('
        lookahead=lexan()
        base()

    elif match(')') is True:
        exp+=')'
        lookahead=lexan()
        base()


    elif ty(lookahead)=='int' or ty(lookahead)=='real':
        exp+=str(lookahead)
        lookahead=lexan()
        base()
    elif lookahead in valList.keys():
        exp+=str(valList[lookahead])
        lookahead=lexan()
        base()
    else:
        return

#WRITE THE CONDITION FUNCTION    
#       <cond>      ::= <oprnd> < <oprnd> |
#                       <oprnd> <= <oprnd> |
#                       <oprnd> > <oprnd> |
#                       <oprnd> >= <oprnd> |
#                       <oprnd> == <oprnd> |
#                       <oprnd> != <oprnd> 

def cond():
    global lookahead
    global op, op2
    op=oprnd()
    lookahead=lexan()
    if match('<'):
        lookahead = lexan()
        op2=oprnd()
        if float(op)<float(op2):
            return True
        else:
            return False
    elif match('<='):
        lookahead = lexan()
        op2=oprnd()
        if float(op)<=float(op2):
            return True
        else:
            return False
    elif match('>'):
        lookahead = lexan()
        op2=oprnd()
        if float(op)>float(op2):
            return True
        else:
            return False
    elif match('>='):
        lookahead = lexan()
        op2=oprnd()
        if float(op)>=float(op2):
            return True
        else:
            return False
    elif match('=='):
        lookahead = lexan()
        op2=oprnd()
        if float(op)==float(op2):
            return True
        else:
            return False
    elif match('!='):
        lookahead = lexan()
        op2=oprnd()
        if float(op)!=float(op2):
            return True
        else:
            return False

#WRITE THE OPERAND FUNCTION ACCORDING TO THE BELOW RULE
#       <oprnd>     ::= id | intnum |realnumber
def oprnd():
    global lookahead
    if ty(lookahead)=='int' or ty(lookahead)=='real':
        return float(lookahead)

    elif lookahead in valList.keys():
        return float(valList[lookahead])


#use the open function to create a buffer to the pointed file
file=open(sys.argv[1],"r")

#read the file from the buffer and store into tokens
tokens=file.read().split()


#get the lexemes one by one
#mitr.next will get the next word
#convert the list into an interatable list mitr
mitr=iter(tokens)


#Lookahead is used to always points to the token one index ahead of the current token
lookahead = lexan()
exp=''
printcount=0
#Call the prog() function to start top down recrusive descent
prog()



