import ply.lex as lex

tokens = ('FOR',
        'DTYPE',
        'LBRACE',
        'LESSER',
        'GREATER',
        'NOT',
        'AND',
        'OR',
        'COMMA',
        'EQUALS',
        'RBRACE',
        'LFLOWER',
        'RFLOWER',
        'NUMBER',
        'ID',
        'SEMICOLON',
        'PLUS',
        'MINUS',
        'DIV',
        'MUL',
        'SHORTHAND',
        )

def t_FOR(t):
    r'for'
    return t

def t_DTYPE(t): 
    r'\b(int|void|char|double|string|bool|float|long|short)\b'
    return t



t_LBRACE = r'\('
t_RBRACE = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'

def t_ID(t):
    r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b'
    return t


def t_PLUS(t): 
    r'\+'
    return t

def t_MINUS(t): 
    r'-'
    return t

def t_MUL(t): 
    r'\*'
    return t


def t_SHORTHAND(t): 
    r'\++|\--'
    return t



def t_DIV(t): 
    r'/'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t


def t_COMMA(t): 
    r','
    return t

t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'=(=)?'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_SEMICOLON = r';'

t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character found {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

data = input()

lexer.input(data)

while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)