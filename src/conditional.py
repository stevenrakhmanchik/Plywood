import g
import errorhandler as eh
from py_expression_eval import Parser

def calculate(var,loc):
    parser = Parser()
    try:
        var = parser.parse(var)
        varsFound = var.variables()
    except:
        eh.ifCondInvalid(loc)
    varDict = {}
    for x in varsFound:
        try:
            a = g.varNames.index(x)
        except:
            eh.ifCondInvalid(loc)
        varDict[x] = g.varValues[a]
    newValue = var.evaluate(varDict)
    return(newValue)

def ifStmt(line):
    loc = g.lineNumber + 1
    ifCondFull = ''
    line_lex = line.split(' ')
    while line_lex[0] != 'THEN':
        line = (g.lines[g.lineNumber]).strip()
        line_lex = line.split(' ')
        if line_lex[0] == "IF":
            if g.ifStmtsFlag == True: eh.ifStmtInBadPlace(g.lineNumber + 1)
        if line_lex[0] != 'THEN': ifCondFull+=line
        g.lineNumber+=1
    if line_lex[0] == "THEN":
        if len(line_lex) != 1:
            eh.thenDoesntTakeArgs(g.lineNumber)
    g.ifStmtsFlag = False
    validity = calculate(ifCondFull,g.lineNumber)
    if validity == True:
        g.nestedIf+=1
        g.do = True
    else:
        g.do = False
    g.lineNumber-=1
