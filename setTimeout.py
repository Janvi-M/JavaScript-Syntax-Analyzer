# parsed_result = parser.parse(js_code)
import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IDENTIFIER',
    'SETTIMEOUT',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
)

t_ignore = ' \t\n'

def t_SETTIMEOUT(t):
    r'setTimeout'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at index {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_statement(p):
    '''
    statement : SETTIMEOUT LPAREN expression COMMA NUMBER RPAREN SEMICOLON
    '''
    print("setTimeout call found with function:", p[3], "and delay:", p[5])

def p_expression_identifier(p):
    '''
    expression : IDENTIFIER
    '''
    p[0] = p[1]

def p_expression_settimeout(p):
    '''
    expression : SETTIMEOUT
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

# Take user input
user_input = input("Enter JavaScript code: ")

# Process user input
lexer.input(user_input)
for token in lexer:
    print(token)

parsed_result = parser.parse(user_input)