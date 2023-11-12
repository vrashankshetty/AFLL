import ply.yacc as yacc

from lexer import tokens

flag = 0

#valid enum declaration

#enum valid {cc,ddd,dd}
def p_declaration(p):
    '''
    declaration : KEYWORD LFLOWER list RFLOWER    
    '''
    p[0] = ('declaration',p[1],p[2])



def p_list(p):
     '''
     list : exp COMMA list
          | exp
          |
     '''


def p_exp(p):
    '''
    exp : ID EQUALS NUMBER
        | ID 
    '''
    
def p_error(p):
    print("Syntax error")
    global flag 
    flag = 1


parser = yacc.yacc()
print("Welcome,You are entering for enum declaration")

while True:
   flag = 0
   try:
       s = input('enter the declaration:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
        print("Result:", result)
        print("VALID SYNTAX")