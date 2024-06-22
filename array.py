import ply.lex as lex
import ply.yacc as yacc

js_keywords = {
    'var': 'VAR',
    'let': 'LET',
    'const':'CONST',
    'new': 'NEW',
    'Array':'ARRAY',
}

start='array_declaration'


tokens = ['ID', 'SEMICOLON', 'LPAREN', 'RPAREN','ASSIGN', 'NUMBER',
            'STRING', 'LBRACKET', 'RBRACKET','COMMA'] + list(js_keywords.values())

t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_STRING = r'"[^"]*"'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA=r'\,'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = js_keywords.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def p_string(p):
    'expression : STRING'
    #print("Valid string:", p[1])

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_array_declaration(p):
    '''array_declaration : CONST ID ASSIGN LBRACKET elements RBRACKET SEMICOLON
                         | CONST ID ASSIGN NEW ARRAY LPAREN RPAREN SEMICOLON
                         | LET ID ASSIGN LBRACKET elements RBRACKET SEMICOLON
                         | LET ID ASSIGN NEW ARRAY LPAREN RPAREN SEMICOLON
                         | LET ID ASSIGN NEW ARRAY LPAREN LBRACKET elements RBRACKET RPAREN SEMICOLON
                         | VAR ID ASSIGN LBRACKET elements RBRACKET SEMICOLON
                         | VAR ID ASSIGN NEW ARRAY LPAREN RPAREN SEMICOLON'''
    print("Valid array declaration in JavaScript")

def p_elements(p):
    '''elements : expression
                | elements COMMA expression'''
    pass

def p_expression(p):
    '''expression : ID
                  | NUMBER
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
