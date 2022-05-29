import g
import errorhandler as eh
from py_expression_eval import Parser

# if var.isalpha():
#     try:
#         a = g.varNames.index(var)
#     except:
#         eh.varDoesntExist(loc)
#     if g.varTypes[a] != "float":
#         eh.wrongTypeInFormat(loc)
#     print(g.varValues[a], end = '')
# elif var.isdecimal():
#     if '.' in var:
#         eh.wrongTypeInFormat(loc)
#     print(var, end = '')

def escape_split(str_to_escape, delimiter='$', escape='\\'):
    if len(delimiter) > 1 or len(escape) > 1:
        raise ValueError("Either delimiter or escape must be an one char value")
    token = ''
    escaped = False
    for c in str_to_escape:
        if c == escape:
            if escaped:
                token += escape
                escaped = False
            else:
                escaped = True
            continue
        if c == delimiter:
            if not escaped:
                yield token
                token = ''
            else:
                token += c
                escaped = False
        else:
            if escaped:
                token += escape
                escaped = False
            token += c
    yield token

def calculate(var,loc):
    parser = Parser()
    try:
        var = parser.parse(var)
        varsFound = var.variables()
    except:
        eh.varDoesntExist(loc)
    varDict = {}
    for x in varsFound:
        try:
            a = g.varNames.index(x)
        except:
            eh.varDoesntExist(loc)
        varDict[x] = g.varValues[a]
    newValue = var.evaluate(varDict)
    return(newValue)

def out(line):
    loc = g.lineNumber + 1
    varMatch = line.strip()
    varMatch = list(escape_split(varMatch, '$'))
    parser = Parser()
    for x in range(0,len(varMatch)):
        var = varMatch[x]
        newValue = calculate(var, loc)
        print(newValue, end = '')

def inp(line):
    loc = g.lineNumber + 1
    return 0
