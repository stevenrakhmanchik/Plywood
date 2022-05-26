from py_expression_eval import Parser
import errorhandler as eh
import g

def declareNum(line):
    parser = Parser()
    acceptable = ('integer','float','numerical')
    banned = ('PI','pi')
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
        varType = g.vars[a]
        if not(varType in acceptable):
            eh.varExistNotNumerical(loc)
        else:
            g.vars.remove(a)
            g.varNames.remove(a)
    g.vars.append([varName, 'numerical', 0.0])
    g.varNames.append(varName)

    varsFound = parser.parse(expression).variables()
    varDict = {}

    for x in varsFound:
        try:
            a = g.varNames.index(x)
        except:
            eh.varDoesntExist(loc)
        if not((g.vars[a])[1] in acceptable):
            eh.varInWrongContext(loc)
        varDict[x] = (g.vars[a])[2]

    newValue = parser.parse(expression).evaluate(varDict)
    if type(newValue) == 'Float': (g.vars[len(g.vars) - 1])[1] = 'float'
    if type(newValue) == 'Int': (g.vars[len(g.vars) - 1])[1] = 'integer'
    if not(g.vars[len(g.vars) - 1])[1] in acceptable:
        eh.declarationNonNumerical(loc)
    (g.vars[len(g.vars) - 1])[2] = newValue
    for x in g.vars:
        print(x)
