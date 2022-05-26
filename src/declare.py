from py_expression_eval import Parser
import errorhandler as eh
import g

def declareNum(line):
    parser = Parser()
    acceptable = ('integer','float','numerical', 'string')
    banned = ()
    line_lex = line.split('->')
    loc = eh.getLine(line) + 1
    expression = line_lex[0]
    varName = line_lex[1].strip()
    if len(line_lex) > 2:
        eh.multiDeclare(loc)
    if varName.isalpha() == False:
        eh.invalidVarName(loc)
    if varName in g.varNames and not(varName in banned):
        a = g.varNames.index(varName)
        varType = g.varTypes[a]
        if not(varType in acceptable):
            eh.varExistNotNumerical(loc)
        else:
            g.varTypes.pop(a)
            g.varValues.pop(a)
            g.varNames.pop(a)
    g.varTypes.append('numerical')
    g.varNames.append(varName)
    g.varValues.append(0.0)
    varsFound = parser.parse(expression).variables()
    varDict = {}
    for x in varsFound:
        try:
            a = g.varNames.index(x)
        except:
            eh.varDoesntExist(loc)
        if not(g.varTypes[a] in acceptable):
            eh.varInWrongContext(loc)
        varDict[x] = g.varValues[a]
    newValue = parser.parse(expression).evaluate(varDict)
    if type(newValue) == type(0.1): (g.varTypes[len(g.varTypes) - 1]) = 'float'
    if type(newValue) == type(1): (g.varTypes[len(g.varTypes) - 1]) = 'integer'
    if not(g.varTypes[len(g.varTypes) - 1]) in acceptable:
        eh.declarationNonNumerical(loc)
    g.varValues[len(g.varValues) - 1] = newValue
