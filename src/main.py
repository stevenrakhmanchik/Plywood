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
import g

def mainLoop(woodFile):
    for g.lineNumber in range(0, len(g.lines)):
        line = g.lines[g.lineNumber]
        line_lex = line.split(' ')
        if line_lex[0] == 'LBL':
            if len(line_lex) != 2: eh.lblTooManyArgs(g.lineNumber + 1)
            label.lbl(line_lex[1])

    g.lineNumber = -1
    while g.lineNumber != len(g.lines):
        g.lineNumber+=1
        line = g.lines[g.lineNumber]
        line_lex = line.strip().split(' ')
        if line_lex[0] == 'LBL':
            continue
        if '->' in line:
            declare.declare(line)
        if line_lex[0] == 'OUT':
            line = line[3:len(line)]
            outin.out(line)
        if line_lex[0] == 'IN':
            line = line[2:len(line)]
            outin.inp(line)
        if line_lex[0] == 'GOTO':
            if len(line_lex) != 2: eh.gotoTooManyArgs(g.lineNumber + 1)
            line = line[4:len(line)]
            g.lineNumber = label.goto(line)


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
            g.lines = [(line.rstrip('\n')) for line in file]
            file.close()

            g.lineNumber = 0
            g.vars = []
            g.varNames = []

            mainLoop(woodFile)
