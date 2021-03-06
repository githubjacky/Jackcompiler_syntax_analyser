TOKEN = ['keyword', 'symbol', 'integerConstant', 'stringConstant', 'identifier']

SYMBOL = '{}()[].,;+-*/&|<>=~'

OP = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=', '~']

UNARYOP = ['-', '~', '&lt;']

KW_CLASS = 'class'
KW_CONSTRUCTOR = 'constructor'
KW_FUNCTION = 'function'
KW_METHOD = 'method'
KW_FIELD = 'field'
KW_STATIC = 'static'
KW_VAR = 'var'
KW_INT = 'int'
KW_CHAR = 'char'
KW_BOOLEAN = 'boolean'
KW_VOID = 'void'
KW_TURE = 'true'
KW_FALSE = 'false'
KW_NULL = 'null'
KW_THIS = 'this'
KW_LET = 'let'
KW_DO = 'do'
KW_IF = 'if'
KW_ELSE = 'else'
KW_WHILE = 'while'
KW_RETURN = 'return'

KEYWORD = [
    KW_CLASS,
    KW_CONSTRUCTOR,
    KW_FUNCTION,
    KW_METHOD,
    KW_FIELD,
    KW_STATIC,
    KW_VAR,
    KW_INT,
    KW_CHAR,
    KW_BOOLEAN,
    KW_VOID,
    KW_TURE,
    KW_FALSE,
    KW_NULL,
    KW_THIS,
    KW_LET,
    KW_DO,
    KW_IF,
    KW_ELSE,
    KW_WHILE,
    KW_RETURN
]

CLASSVAR_TYPE = [KW_STATIC, KW_FIELD]

VAR_TYPE = [KW_INT, KW_CHAR, KW_BOOLEAN]

SUBROUTINE_TYPE = [KW_CONSTRUCTOR, KW_FUNCTION, KW_METHOD]

STATEMENT_TYPE = [KW_LET, KW_IF, KW_ELSE, KW_WHILE, KW_DO, KW_RETURN]

KEYWORD_CONSTANT = [KW_TURE, KW_FALSE, KW_NULL, KW_THIS]