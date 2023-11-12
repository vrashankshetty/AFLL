import ply.yacc as yacc
from lexer import tokens

flag = 0

def p_while(p):
    '''
    for_statement     : FOR LBRACE initialization  SEMICOLON conditions SEMICOLON iteration RBRACE LFLOWER statements RFLOWER
                      | FOR LBRACE initialization  SEMICOLON conditions SEMICOLON iteration RBRACE singleStatement 
    '''
    # if len(p) == 6:
    #     p[0] = (p[1],p[3],p[5])
    # else:
    #     p[0] = (p[1],p[3],p[6])

    
def p_initialization(p):
    '''
    initialization  : DTYPE ID EQUALS NUMBER
                    |
    '''
    
def p_conditions(p):
    '''
    conditions  : ID EQUALS data 
                | ID GREATER data 
                | ID LESSER data 
                | ID GREATER EQUALS data 
                | ID LESSER EQUALS data 
                | ID NOT EQUALS data
                | conditions AND conditions 
                | conditions OR conditions
                | data
                |
    '''
    
def p_data(p):
    '''
    data : ID 
        | NUMBER
    '''    


def p_iteration(p):
    
    '''
    iteration  : ID EQUALS ID PLUS NUMBER 
               | ID EQUALS ID MINUS NUMBER 
               | ID EQUALS ID MUL NUMBER 
               | ID EQUALS ID DIV NUMBER
               | ID SHORTHAND
               |
    '''


def p_statements(p):
    '''
    statements  : statements statement
                | statement
    '''
    # if len(p) == 2:
    #     p[0] = (p[1],)
    # else:
    #     p[0] = p[1]+(p[2],)

def p_statement(p):
    '''
    statement   : list SEMICOLON
                | for_statement
                | empty
    '''


def p_singleStatement(p):
    '''
    singleStatement  : list SEMICOLON 
                    | empty
                    | for_statement
    '''
 

def p_list(p):
    '''
    list    : ID list
            | ID
    '''

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None




def p_error(p):
    print("Syntax error",p)
    global flag 
    flag = 1


print("Welcome,You are entering for loop declaration")
parser = yacc.yacc()
while True:
   flag = 0
   try:
       s = input('enter the conditional statement:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
        print("Valid syntax")
        print("Result:", result)
