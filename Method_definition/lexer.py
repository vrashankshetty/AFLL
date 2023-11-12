import ply.lex as lex

#define TOKENS
# <public>(optional) <static>(optional) <datatype> <funcname> <(params)> <semicolon>{<code> return t}
tokens = ('DTYPE',
          'ID',
          'LBRACE',
          'RBRACE',
          'COMMA',
          'SEMICOLON',
          'LFLOWER',
          'RFLOWER',
          'PUBLIC',
          'PROTECTED',
          'PRIVATE',
          'OVERRIDE',
          'STATIC',
          'SEALED',
          'PARTIAL',
          'VIRTUAL',
          'ABSTRACT',
          )

def t_PUBLIC(t):
    r'public'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PRIVATE(t):
    r'private'
    return t



def t_OVERRIDE(t):
    r'override'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_PARTIAL(t):
    r'partial'
    return t

def t_SEALED(t):
    r'sealed'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t




def t_DTYPE(t): 
    r'\b(int|void|char|double|string|bool|float|long|short)\b'
    return t



def t_ID(t):
    r'\b[a-zA-z_][a-zA-Z0-9_]*\b' 
    return t


t_LBRACE = r'\('
t_RBRACE = r'\)'


def t_COMMA(t):
    r','
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LFLOWER(t):
    r'{'
    return t


def t_RFLOWER(t):
    r'}'
    return t



t_ignore = ' \t\n'



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