import ply.lex as lex
import ply.yacc as yacc

js_keywords = {
    'var': 'VAR',
    'let': 'LET',
    'for': 'FOR',
    'console' : 'CONSOLE',
    'log':'LOG'
}

tokens = ['ID', 'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'ASSIGN', 'NUMBER', 'GT', 'LT', 'PLUS', 'MINUS', 'DQ','DOT'] + list(js_keywords.values())

t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_GT = r'\>'
t_LT = r'\<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DQ = r'\"'
t_DOT = r'\.'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = js_keywords.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_for_loop(p):
    'for_loop : FOR LPAREN variable_declaration SEMICOLON expression SEMICOLON assignment RPAREN LBRACE print SEMICOLON RBRACE'
    print("Valid for loop in JavaScript")

def p_print(p):
    '''print : CONSOLE DOT LOG LPAREN DQ ID DQ RPAREN
    |
    '''


def p_variable_declaration(p):
    '''variable_declaration : VAR ID
                            | LET ID
                            | VAR ID ASSIGN NUMBER
                            | LET ID ASSIGN NUMBER
                            | ID ASSIGN NUMBER
                            | ID
                            |
    '''

def p_expression(p):
    '''expression : ID
                  | ID GT NUMBER
                  | ID LT NUMBER
                  | ID GT ID
                  | ID LT ID
                  | ID GT ASSIGN ID
                  | ID GT ASSIGN NUMBER
                  | NUMBER GT ASSIGN ID 
                  | NUMBER GT ASSIGN NUMBER
                  | ID LT ASSIGN NUMBER
                  | ID LT ASSIGN ID
                  | NUMBER LT ASSIGN ID
                  | NUMBER LT ASSIGN NUMBER
                  |
    '''

def p_assignment(p):
    '''assignment : ID ASSIGN ID
                  | ID ASSIGN NUMBER
                  | ID PLUS PLUS
                  | ID MINUS MINUS
                  |
    '''

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    try:
        s = input("Enter JavaScript code: ")
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)