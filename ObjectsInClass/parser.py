import ply.yacc as yacc
from lexer import tokens

flag = 0

def p_declaration(p):
    '''
    declaration : ID EQUALS NEW LEFTBRACE RIGHTBRACE SEMICOLON
    '''
    p[0] = ('declaration', p[1], p[3])

def p_error(p):
    print("Syntax error", p)
    global flag 
    flag = 1

parser = yacc.yacc()

print("Welcome, You are entering for array declaration")

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