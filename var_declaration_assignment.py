import ply.lex as lex
import ply.yacc as yacc

js_keywords = {
    'var': 'VAR',
    'let': 'LET',
    'const': 'CONST',
}

tokens = ['ID', 'SEMICOLON', 'ASSIGN', 'NUMBER'] + list(js_keywords.values())

t_SEMICOLON = r';'
t_ASSIGN = r'='
t_NUMBER = r'\d+'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = js_keywords.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_statement(p):
    '''statement : variable_declaration
                 | variable_assignment
                 '''
    print("Statement is correct.")

def p_variable_declaration(p):
    '''variable_declaration : VAR ID SEMICOLON
                            | LET ID SEMICOLON
                            | CONST ID SEMICOLON
                            '''
    print("Variable declaration is correct.")

def p_variable_assignment(p):
    '''variable_assignment : VAR ID ASSIGN expression SEMICOLON
                           | LET ID ASSIGN expression SEMICOLON
                           | CONST ID ASSIGN expression SEMICOLON
                           | VAR ID SEMICOLON ID ASSIGN expression SEMICOLON
                           | LET ID SEMICOLON ID ASSIGN expression SEMICOLON
                           | CONST ID SEMICOLON ID ASSIGN expression SEMICOLON
                           '''
    print("Variable assignment is correct.")

def p_expression(p):
    '''expression : ID
                  | NUMBER
                  '''
    # You can add more cases for expressions as needed

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    try:
        s = input("Enter JavaScript code (Ctrl+D to exit): ")
    except EOFError:
        break
    if not s:
        continue

    parser.parse(s)