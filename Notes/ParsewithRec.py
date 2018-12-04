#first(alpha)={a|alpha-->a Beta} where a beta is terminal
# LEFT RECURSION IS NOT SUTIABLE FOR TOP DOWN RECURSIVE DESCENT
# MUST CONVERT LEFT RECURSION TO RIGHT RECURSION
#   Conversion: <A>--><A> Alpha | Beta
#   Right   <A>-->Beta <A'>
#           <A'>-->Alpha <A'> | Epsilon      where epsilon reps Empty
#
def A()
    match('Beta')
    Aprime()

    
def Aprime(){
    if lookahead=='Alpha'
        match('Alpha')
        Aprime()
    elif
        #empty case
    
#RULES
# <E>--><E>+<T>|<E>-<T>|<T>
# <T>--><T>*<F>|<T>/<F>|<F>
# <F>-->ID|(<E>)
#
# Rewritten for right recursion
# <E>--> <T> <E'>
# <E'>--> + <T> <E'> | - <T> <E'>|epsilon   where esilon reps empty
#
# BNF--> EBNF (Extended) use loop
# <E>--> <T> {(+|-)<T>}   these will be repeated zero or more times
#                   aka:  - <T> + <T> + <T>
#
#<T>--><F>{(*|/)<F>} 
#<F>-->ID| '('<E>')'
