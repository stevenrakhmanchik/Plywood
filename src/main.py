#    ___ _                               _
#   / _ \ |_   ___      _____   ___   __| |
#  / /_)/ | | | \ \ /\ / / _ \ / _ \ / _` |
# / ___/| | |_| |\ V  V / (_) | (_) | (_| |
# \/    |_|\__, | \_/\_/ \___/ \___/ \__,_|
#          |___/
# Steven Rakhmanchik (C) 2022 Plywood Programming Language
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
import sys
import os.path
import errorhandler as eh
import declare
import outin
import label
import conditional
import g
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def mainLoop(woodFile):
    linesReplace = []
    for g.lineNumber in range(0, len(lines)):
        line = lines[g.lineNumber]
        multilines = list(outin.escape_split(line, ";", "\\"))
        oneLine = []
        for x in multilines:
            x = x.strip()
            line_lex = x.split(' ')
            oneLine.append(x)
            if x[0:2] == "IF":
                if len(multilines) != 1: eh.ifMustBeAlone(g.lineNumber + 1)
            if x[0:4] == "THEN":
                if len(multilines) != 1: eh.thenMustBeAlone(g.lineNumber + 1)
            if x[0:4] == "GOTO":
                if len(multilines) != 1: eh.gotoMustBeAlone(g.lineNumber + 1)
            if x[0:3] == "LBL":
                if len(multilines) != 1: eh.lblMustBeAlone(g.lineNumber + 1)
                if len(line_lex) != 2: eh.lblTooManyArgs(g.lineNumber + 1)
                label.lbl(line_lex[1])
        g.lines.append(oneLine)
    g.lineNumber = -1
    g.ifStmtsFlag = False
    g.lines.append('')
    while g.lineNumber != len(g.lines) -1:
        g.lineNumber+=1
        code = g.lines[g.lineNumber]
        for line in code:
            run(line)

def run(line):
    line_lex = line.split(' ')
    if g.do == True:
        # if line_lex[0] == 'LBL':
        #     g.lineNumber+=1
        #     code = g.lines[g.lineNumber]
        #     for line in code:
        #         print(line)
        if '->' in line:
            declare.declare(line)
        if line_lex[0] == 'OUT':
            line = line.strip()
            line = line[3:len(line)].strip()
            outin.out(line)
        if line_lex[0] == 'IN':
            line = line[2:len(line)]
            outin.inp(line)
        if line_lex[0] == 'GOTO':
            if len(line_lex) != 2: eh.gotoTooManyArgs(g.lineNumber + 1)
            line = line[4:len(line)].strip()
            g.lineNumber = label.goto(line)

        if line_lex[0] == 'IF':
            if not(len(line_lex) == 1): eh.ifDoesntTakeArgs(g.lineNumber + 1)
            if g.ifStmtsFlag == True: eh.ifStmtInBadPlace(g.lineNumber + 1)
            g.ifStmtsFlag = True
            g.lineNumber+=1
            line = (g.lines[g.lineNumber])[0]
            conditional.ifStmt()
        elif line_lex[0] == 'ENDIF' and g.nestedIf == 0:
            eh.endifWithNoIf(loc)

    if line_lex[0] == 'ELSE':
        if not(len(line_lex) == 1): eh.elseDoesntTakeArgs(g.lineNumber + 1)
        g.do = not g.do
        g.nestedIf+=1

    if line_lex[0] == 'ENDIF' and (g.nestedIf > 0 or g.do == False):
        if not(len(line_lex) == 1): eh.endifDoesntTakeArgs(g.lineNumber + 1)
        g.nestedIf-=1
        g.do = True

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
if (len(sys.argv)) != 2:
    eh.noFileArg()
else:
    woodFile = sys.argv[1]
    if woodFile[len(woodFile)-5:len(woodFile)] != ".wood":
        eh.noWoodFileArg()
    else:
        if os.path.exists(woodFile) == False:
            eh.noWoodFileExist()
        else:
            file = open(woodFile, "r")
            lines = [(line.rstrip('\n')) for line in file]
            file.close()

            g.lineNumber = 0
            g.vars = []
            g.varNames = []
            mainLoop(woodFile)
