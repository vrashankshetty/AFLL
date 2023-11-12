

import ply.lex as lex


#valid array declaration is c# is that it is always allocated dynmaically 

#so this int [10]num is invalid whereas int []num is valid;


tokens = ('DTYPE',
        'ID',
        'RIGHTBRACE',
        'LEFTBRACE',
        'COMMA',
        'SEMICOLON')

def t_DTYPE(t): 
    r'\b(int|char|double|string|bool|float|long|short)\b'
    return t

def t_ID(t):
    r'\b[a-zA-z_][a-zA-Z0-9_]*\b' 
    return t

def t_COMMA(t):
    r',' 
    return t

t_LEFTBRACE = r'\['
t_RIGHTBRACE = r'\]'


def t_SEMICOLON(t):
    r';'
    return t
t_ignore = ' \t'



def t_error(t):
    print(f"Illegal character encountered {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

data = input()

lexer.input(data)

while(1):
     tok = lexer.token()
     if not tok:
         break
     print(tok)