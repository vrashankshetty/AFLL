import ply.lex as lex

tokens = (
    'EQUALS',
    'CLASSNAME',
    'ID',
    'RIGHTBRACE',
    'LEFTBRACE',
    'NEW',
    'SEMICOLON',
)


def t_NEW(t):
    r'new'
    return t


def t_CLASSNAME(t):
    r'\b([A-Z_][a-zA-Z_0-9]*)\b'
    return t


def t_ID(t):
    r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b'
    return t


t_LEFTBRACE = r'\('
t_RIGHTBRACE = r'\)'


def t_EQUALS(t):
    r'='
    return t


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

